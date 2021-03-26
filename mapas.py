"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python sao representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
# Iterar sobre dicionarios

print('\nImprime a chave')
for chave in receita:
    print(chave)

print('\nImprime o valor de chave')
for chave in receita:
    print(receita[chave])

print('\nImprime a chave e valor')
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')


# Acessando as chaves

print(receita.keys())


for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


# Soma, valor maximo, valor minimo, tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))