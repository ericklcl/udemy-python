"""
Conjuntos

- Conjuntos em qualquer linguagem de programacao, estamos fazendo referência à Teoria dos Conjuntos
da Matemática.

- Aqui no Python, os conjuntos sao chamados de Sets.

Dito isto, da mesma forma que na matematica:
- Sets (conjuntos) nao possuem valores duplicados.
- Sets (conjuntos) nao possuem valores ordenados.
- Elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos mas não nos importamos
com a ordenacao deles. 
Quando nao precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) sao referenciados em python com chaves {}

Diferença entre conjuntos(sets) e mapas(dicionarios) em python:
- Um dicionario tem chave/valor
- Um conjunto tem apenas valor
"""

# Definindo um conjunto

# Forma 1
print("\n# Forma 1")
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare aqui que temos valores repetidos
print(s)
print(type(s))

# Forma 2 - Mais comum
print("\n# Forma 2")
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

s = set('Geek University')
print(s)

lista = [1, 2, 3, 4, 5, 6, 6, 8, 8]
s = set(lista)
print(s)

tupla = (1, 2, 3, 5, 5, 7)
s = set(tupla)
print(s)


# Podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('tem o 3')
else:
    print('nao tem o 3')


# Importante lembrar que alem de nao termos valores duplicados, nao temos ordem no set
print("\n\n")
lista = [99, 2, 2, 34, 23, 34, 12, 1, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 2, 34, 23, 34, 12, 1, 44, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 2, 34, 23, 34, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')



