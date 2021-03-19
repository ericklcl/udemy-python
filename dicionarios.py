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
