"""
Documentando funcoes com Docstrings
"""


# Exemplos

def diz_oi():
    """uma funcao simples que retorna a string Oi"""
    return 'oi'


# print(diz_oi())

# print(diz_oi.__doc__)

# print(help(diz_oi))

# print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de numero ou 'numero' a potencia informada.
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial. Por padrao é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia


print(help(exponencial))
