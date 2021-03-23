"""
Dicionarios sao colecoes do tipo chave/valor

Dicionarios sao representados por chaves {}.
"""

print(type({}))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Criação de dicionarios

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

# Acessando elementos em um dicionario

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print("\nForma 1 - Acessando via chave, da mesma forma que lista/tupla")
print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get - Recomendada
print("\nForma 2 - Acessando via get - Recomendada")
print(paises.get('br'))
print(paises.get('ru'))

russia = paises.get('ru')

pais = paises.get('py')
if pais:
    print(f'Encontrei o pais {pais}'.format(pais=pais))
else:
    print(f'Nao encontrei o pais {pais}')

# Eh possivel definir um valor padrao para o dicionario usando o get, caso nao encontremos o objeto com a chave
# informada

pais = paises.get('ru', 'Nao encontrado')
print(f'Encontrei o pais {pais}'.format(pais=pais))

pais = paises.get('py', 'Nao encontrado')
print(f'Encontrei o pais {pais}'.format(pais=pais))

# Caso o get nao encontre o objeto com a chave informada, será retornado o valor None e não será gerado KeyError

# Podemos verificar se determinada chave se encontra em um dicionario
print("\n### verificando se a chave existe no dicionario ###")
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises.get('ru')
print(russia)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionario como chaves de dicionarios.
# Tuplas são bastante interessantes de serem utilizadas como chave de dicionario, pois as mesmas são imultaveis.
localidades = {
    (35.6895, 39.6917) : 'Escritorio em Tokio',
    (40.7128, 74.0060) : 'Escritorio em Nova York',
    (35.6895, 122.4194) : 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionario
print("\n ### Adicionar elementos em um dicionario ###")
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 (mais comum)
print('\nForma 1 - Adicionar elementos em um dicionario')
receita['abr'] = 350
print(receita)

# Forma 2
print('\nForma 2 - Adicionar elementos em um dicionario')
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1
print("\n### Atualizando dados em um dicionario - Forma 1 ###")
print(receita)
receita['mai'] = 550
print(receita)

# Forma 2
print("\n### Atualizando dados em um dicionario - Forma 2 ###")
receita.update({'mai':600})
print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario eh a mesma
# CONCLUSAO 2: Em dicionarios, NAO podemos ter chaves repetidas
