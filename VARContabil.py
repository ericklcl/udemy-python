# -*- coding: utf-8 -*-
"""
Autor: Iure Barros
Data: 16/04/2021
Versao: 1.0
Iniciativa: VAR Contabil
Classe Desc.: Essa classe recebe um histórico de 5 anos de lançamentos contábeis e busca identificar
anomalias nos lançamentos a partir de métodos baseados na definição de outliers."
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import ruptures as rp
import datetime as dt
from pyspark.sql import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("VArContabil") \
    .getOrCreate()


def clean_outliers(val, k=1.5):
    """
    Retorna uma lista de lançamentos após a exclusão dos outliers identificados.
    :param val: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :param k: Constante de sensibilidade do outlier. O valor padrão é 1.5.
    :return: Lista de valores com a exclusão dos outliers.
    """
    q1, q3 = np.percentile(val, [25, 75])
    h = k * (1.100 * q3 - 0.900 * q1)
    val = [n for n in val if ((n < q3 + h) and (n > q1 - h))]
    return val


def chgpt(val):
    """
    Retorna uma lista com os indicadores onde existe uma mudança na curva do comportamento do
    indicador. 1 (um) para uma mudança de comportamento e 0 (zero) para um comportamento que se manteve.
    :param val: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :return: Lista de valores com os valores dos lançamentos e os resultados dos comportamentos.
    """
    n = len(val)
    val = np.array(val)
    sigma = np.std(val) ** 0.5
    algo = rp.Pelt(model="l2", min_size=5).fit_predict(val, pen=np.log(n) * 2 * sigma ** 2)
    change_points = [0 for i in val]
    for i in range(len(algo)):
        if algo[i] != len(val):
            change_points[algo[i]] = 1
    return change_points


def last(ls, value):
    """
    Retorna a posição da última ocorrência do valor na lista dos lançamentos contábeis.
    :param ls: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :param value: Valor a ser buscado na lista de lançamentos contábeis.
    :return: Posição (índice) do valor buscado na lista de lançamentos contábeis.
    """
    try:
        a = len(ls) - 1 - ls[::-1].index(value)
    except:
        a = 0
    return a


def outlier(val, dif, var, k=1.5):
    """
    Identifica valores outliers em uma curva de forma retorativa e considerando o seu comportamento mais recente.
    Retorna a lista de indicadores de variação (1 para valores considerados como outlier,
    0 para valores normais), atualizada indicando se o valor é um outlier considerando o
    grupo de valores anteriores a ele.
    :param val: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :param dif: Lista das derivadas dos lançamentos contábeis.
    :param var: Lista dos indicadores de variação dos lançamentos contábeis.
    :param k: Constante de sensibilidade do outlier. O valor padrão é 1.5.
    :return: Lista de indicadores de variação (1 para valores considerados como outlier,
    0 para valores normais), atualizada indicando se o valor é um outlier considerando o
    grupo de valores anteriores a ele.
    """
    lista_valores = []
    lista_dif = []
    var = var
    record = []
    for i in range(len(val)):
        if var[i] == 0:
            lista_valores.append(val[i])
            lista_dif.append(dif[i])
            if len(lista_valores) > 5:
                chg = chgpt(lista_valores)
                pointchg = last(chg, 1)
                lista_valores_esp = lista_dif[pointchg:]
                record.append(len(lista_valores_esp))
                q3, q1 = np.percentile(lista_valores_esp, [75, 25])
                iqr = q3 - q1
                minimo = q1 - (iqr * k)
                maximo = q3 + (iqr * k)
                if dif[i] < minimo or dif[i] > maximo:
                    var[i] = 1
            else:
                record.append(0)
        else:
            record.append(0)
    return var


def deriva(lista_valores):
    """
    :param lista_valores: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :return: Retorna uma lista de quanto a variação entre um ponto em relação ao ultimo valor.
    Para caso de divisão por 0, o valor é 100 caso o numerador seja positivo, -100 para
    numerador negativo e 0 para caso o numerador seja 0.
    """
    lista_dif = [0 for i in range(len(lista_valores))]
    for i in range(len(lista_valores)):
        if i > 0:
            dif = float(lista_valores[i]) - float(lista_valores[i - 1])
            if lista_valores[i - 1] != 0 and lista_valores[i] != 0:
                perc = (dif / float(lista_valores[i - 1])) * 100
                lista_dif[i] = perc
            else:
                if dif > 0:
                    perc = 100
                else:
                    if dif < 0:
                        perc = -100
                    else:
                        perc = 0
                lista_dif[i] = perc
    return lista_dif


def avg(a):
    """
    Calcula a média dos valores da lista
    :param a: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :return: Retorna a média dos valores de entrada.
    """
    med = sum(a) / len(a)
    return med


def predict(lista):
    """
    Calcula a previsão do valor esperado baseado em uma regressão dos últimos 4 pontos.
    :param lista: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :return: Retorna uma lista com a variação entre o valor real e o previsto em cada ponto (var),
    e uma lista (var_perc) com o quanto essa variação representa em percentual em relação aos valores da lista val.
    """
    a = []

    for i in range(len(lista)):
        y = lista[:i + 1]
        if len(y) > 2:
            if len(clean_outliers(y[-6:-1])) >= 2:
                b = clean_outliers(y[-6:-1])
            else:
                b = y[-6:-1]
            t = np.array((range(len(b))))
            b = np.array(b)
            t = t.reshape(-1, 1)
            b = b.reshape(-1, 1)
            model = LinearRegression().fit(t, b)
            a.append(model.predict(np.array(len(b)).reshape(-1, 1)))
        else:
            a.append(y[i])
    var = [abs(a - i) for a, i in zip(a, lista)]
    var = [float(i) for i in var]
    var_perc = [j / k if k != 0 else 10 for j, k in zip(var, a)]
    var_perc = [float(i) for i in var_perc]
    return var, var_perc


def esqueceu_mes(deb, cred, var):
    """
    Identifica os meses onde não ocorreram lançamentos após um período de três meses consecutivos onde houve
    lançamento.
    :param deb: Lista de valores de lançamentos contábies de débito.
    :param cred: Lista de valores de lançamentos contábeis de crédito.
    :param var: Lista com os indicadores de variação de lançamento.
    :return: Retorna a lista de indicadores de variação atualizada, indicando meses sem
    nenhum lançamento que vieram após 3 meses que ocorreram lançamentos.
    """
    for i in range(len(deb)):
        if i > 3:
            if ((deb[i - 1] != 0 and deb[i - 2] != 0 and deb[i - 3] != 0) or (
                    cred[i - 2] != 0 and cred[i - 3] != 0 and cred[i - 1] != 0)) and (deb[i] == 0 and cred[i] == 0):
                var[i] = 1
    return var


def comparador(val):
    """
    :param val: Lista de lançamentos contábeis de uma determinada conta e subconta.
    :return: Retorna uma lista de quanto a variação entre um ponto em relação ao ultimo valor.
    Não possui tratamento para valores infinitos.
    """
    c = []
    for i in range(len(val)):
        va = val[:i + 1]
        if len(va) > 2:
            a = va[-1] - va[-2]
            b = va[-1]
            c.append(a / b)
        else:
            c.append(0)
    return c


def distinct(lt):
    """
    Lista de valores distintos com base na entrada de dados.
    :param lt: Lista dos lançamentos contábeis.
    :return: Retorna uma lista dos valores de entrada de forma distinta.
    """
    lt_dist = []
    for x in lt:
        if x not in lt_dist:
            lt_dist.append(x)
    return lt_dist


def datas(a):
    """
    Realiza a conversão da data informada como entrada.
    :param a: Data de entrada como string
    :return: Retorna a data no formato date/time.
    """
    try:
        a = dt.datetime.strptime(a, '%d/%m/%Y %H:%M:%S').date()
    except:
        try:
            a = dt.datetime.strptime(a, '%Y-%m-%d %H:%M:%S').date()
        except:
            try:
                a = dt.datetime.strptime(a, '%Y-%m-%d').date()
            except:
                try:
                    a = dt.datetime.strptime(a, '%d/%m/%Y').date()

                except:
                    try:
                        a = dt.datetime.strptime(a, '%d-%m-%Y').date()
                    except:
                        a = dt.datetime.strptime(a, '%d/%m/%y').date()
    return a


if __name__ == "__main__":
    """
    Entry point para a execução do modelo preditivo.
    """

    rawdf_fill = spark.read.jdbc("jdbcUrl", table="VARCONT_SA_SICON060_9_AGG_AUX")
    rawdf_desc = spark.read.jdbc("jdbcUrl", table="VARCONT_SA_CTA_SCT")
    rawdf_time = spark.read.jdbc("jdbcUrl", table="varcont_sa_timeline")

    # TRATAMENTO DAS BASES
    df_fill = rawdf_fill.toPandas()
    df_fill["ContaSub"] = df_fill["CODCTA_CTB_LCT"].apply(str) + "-" + df_fill["CODSCT_CTB_LCT"].apply(str)
    df_desc = rawdf_desc.toPandas()
    df_desc["ContaSub"] = df_desc["CODCTA_CTB"].apply(str) + "-" + df_desc["CODSCT_CTB"].apply(str)
    df_time = rawdf_time.toPandas()

    df_fill.TOTVAL_DEB_CS.fillna("0", inplace=True)
    df_fill.TOTVAL_CRD_CS.fillna("0", inplace=True)
    df_fill.SLDVAL_CS.fillna("0", inplace=True)
    df_desc.COD_EMPRESA.fillna("191", inplace=True)

    df_fill["MESCTZ_LCT"] = df_fill["MESCTZ_LCT"].astype(int)
    df_desc["MESCTZ_CS"] = df_desc["MESCTZ_CS"].astype(int)
    df_fill["ANOCTZ_LCT"] = df_fill["ANOCTZ_LCT"].astype(int)
    df_desc["ANOCTZ_CS"] = df_desc["ANOCTZ_CS"].astype(int)
    df_fill["COD_EMPRESA"] = df_fill["COD_EMPRESA"].astype(int)
    df_desc["COD_EMPRESA"] = df_desc["COD_EMPRESA"].astype(int)
    df_time["COD_EMPRESA"] = df_time["COD_EMPRESA"].astype(int)
    df_time["IND_RECEITA"] = df_time["IND_RECEITA"].astype(int)

    df_desc.sort_values(['ContaSub', "MES_REF"], inplace=True)
    df_desc.reset_index(inplace=True, drop=True)
    df_descricao = df_desc.groupby("ContaSub").last()
    df_descricao.reset_index(inplace=True)
    df_temp = pd.merge(df_fill, df_desc[["ContaSub", "MES_REF", "COD_CVM", "SALDO_INVERTIDO"]],
                       left_on=["ContaSub", "MES_ANO_CTZ_LCT"], right_on=["ContaSub", "MES_REF"])
    df_temp = pd.merge(df_temp, df_time, on="COD_CVM")
    df_inicial = pd.DataFrame()
    for ano in list(df_temp["ANOCTZ_LCT"].unique()):
        df_ano = df_temp[df_temp["ANOCTZ_LCT"] == ano]
        for mes in list(df_temp["MESCTZ_LCT"].unique()):
            df_mes = df_ano[df_ano["MESCTZ_LCT"] == float(mes)]
            df_mes["Faturamento_Medio"] = sum(
                df_ano[(df_ano["MESCTZ_LCT"] <= float(mes)) & (df_temp["IND_RECEITA"] == 1)]["mov"]) / mes
        df_inicial = df_inicial.append(df_mes)
        df_inicial.drop(columns=["COD_EMPRESA_y"], inplace=True)
        df_inicial.rename(columns={"COD_EMPRESA_x": "COD_EMPRESA"}, inplace=True)

    # Tabela base
    df_inicial = df_inicial.sort_values(['ContaSub', 'ANOCTZ_LCT', 'MESCTZ_LCT'])
    df_inicial.reset_index(drop=True, inplace=True)

    # Lista de contas-subcontas a serem analisadas
    lista_contasub = list(set(df_inicial["ContaSub"].values))

    # Tabela utilizada para consolidar os dados analisados
    df_final = pd.DataFrame()

    # Loop para analisar cada conta/subconta
    for contasub in lista_contasub:

        # Filtra tabela para cada conta/subconta
        df_filtro = df_inicial[(df_inicial["ContaSub"] == contasub)]
        df_filtro.reset_index(drop=True, inplace=True)

        # Verifica o valor a ser analisado (movimentação ou saldo)
        # Contas iniciadas com 1 ou 2 devem utilizar o saldo para análise e as demais
        # contas devem utilizar a movimentação
        if str(contasub[0]) == '1' or str(contasub[0]) == '2':
            df_filtro['val_analise'] = df_filtro["SLDVAL_CS"].values
        else:
            df_filtro['val_analise'] = df_filtro["mov"].values
            df_filtro = df_filtro.sort_values(['ANOCTZ_LCT', 'MESCTZ_LCT'])
            lista_valores = list(df_filtro["val_analise"].values)

    lista_dif = deriva(lista_valores)

    var = [0 for i in range(len(lista_valores))]
    var = outlier(lista_valores, lista_dif, var, 1.5)
    var = esqueceu_mes(df_filtro["TOTVAL_DEB_CS"].values.tolist(), df_filtro["TOTVAL_CRD_CS"].values.tolist(), var)

    df_filtro['dif'] = lista_dif
    df_filtro['IND_OUTLIER'] = var

    dif_media, dif_perc = predict(lista_valores)
    df_filtro["Variacao"] = dif_media
    df_filtro["PERC_VARIACAO_VLR_MEDIO"] = dif_perc
    df_filtro["PERC_VARIACAO_FAT_EMP"] = [abs(a * c / b) if b != 0 else 0 for a, b, c in
                                          zip(dif_media, df_filtro['Faturamento_Medio'].values.tolist(),
                                              df_filtro['IND_OUTLIER'].values.tolist())]
    df_filtro["PERC_VARIACAO_VLR_MEDIO"] = [abs(a * b) for a, b in
                                            zip(dif_perc, df_filtro['IND_OUTLIER'].values.tolist())]
    df_filtro["PERC_VARIACAO_ULT_2_MESES"] = comparador(lista_valores)
    df_final = df_final.append(df_filtro)

    # %%
    lista_meses = df_final.MES_ANO_CTZ_LCT.unique().tolist()
    lista_meses.sort()
    df_out = df_final[(df_final["MES_ANO_CTZ_LCT"] == lista_meses[-2]) |
                      (df_final["MES_ANO_CTZ_LCT"] == lista_meses[-1])]
    df_out["DATA_CGA"] = dt.datetime.now()
    df_out = df_out[["COD_EMPRESA", "MES_ANO_CTZ_LCT", "CODCTA_CTB_LCT", "CODSCT_CTB_LCT", "COD_CVM", "SALDO_INVERTIDO",
                     "TOTVAL_DEB_CS", "TOTVAL_CRD_CS", "SLDVAL_CS", "PERC_VARIACAO_VLR_MEDIO", "PERC_VARIACAO_FAT_EMP",
                     "PERC_VARIACAO_ULT_2_MESES", "DATA_CGA", "IND_OUTLIER"]]

    df_out.reset_index(drop=True, inplace=True)
    df_out.fillna(0, inplace=True)
    df_out.replace(np.inf, 999, inplace=True)
    df_out.replace(-np.inf, 999, inplace=True)

    df_out["DATA_CGA"] = df_out["DATA_CGA"].astype(str)
    df_out["MES_ANO_CTZ_LCT"] = df_out["MES_ANO_CTZ_LCT"].astype(str)

    mySchema = StructType([StructField("COD_EMPRESA", IntegerType(), True),
                           StructField("MES_ANO_CTZ_LCT", StringType(), True),
                           StructField("CODCTA_CTB_LCT", StringType(), True),
                           StructField("CODSCT_CTB_LCT", StringType(), True),
                           StructField("COD_CVM", StringType(), True),
                           StructField("SALDO_INVERTIDO", StringType(), True),
                           StructField("TOTVAL_DEB_CS", FloatType(), True),
                           StructField("TOTVAL_CRD_CS", FloatType(), True),
                           StructField("SLDVAL_CS", FloatType(), True),
                           StructField("PERC_VARIACAO_VLR_MEDIO", FloatType(), True),
                           StructField("PERC_VARIACAO_FAT_EMP", FloatType(), True),
                           StructField("PERC_VARIACAO_ULT_2_MESES", FloatType(), True),
                           StructField("DATA_CGA", StringType(), True),
                           StructField("IND_OUTLIER", IntegerType(), True)])

    sdf = spark.createDataFrame(df_out, schema=mySchema)

    sdf.write.jdbc("jdbcUrl", table="varcont_sa_result_modelo", mode="append")
