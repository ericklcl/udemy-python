"""
Modulo Collections - Ordered Dict
"""

# Em um dicionario a ordem de insercao dos elementos nao eh garantida
lista = [('a',1),('b',2), ('c',3), ('d',4), ('e',5)]

dicionario = dict(lista)

print("Dicionario")
for chave, valor in dicionario.items():
    print(f'chave={chave} e valor={valor}')


from collections import OrderedDict

dicionario2 = OrderedDict(lista)

print("OrderedDict")
for chave, valor in dicionario2.items():
    print(f'chave={chave} e valor={valor}')


# Entendendo a diferenca entre Dicionario e Ordered Dict

# Testando dicionarios normais
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}

print("\n# Testando dicionarios normais")
print(dic1 == dic2) # True - Ja que a ordem dos elementos nao importa para o dicionario


# Testando Ordered Dict
print("\n# Testando Ordered Dict")
dic1 = OrderedDict({'a': 1, 'b': 2})
dic2 = OrderedDict({'b': 2, 'a': 1})
print(dic1 == dic2) # False - Ja que a ordem dos elementos iporta em um ordered dict

