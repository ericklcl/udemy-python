print("\nExemplo1 - Tupla")
tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))
print(tupla1)

print("\nExemplo2 - Tupla")
tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))
print(tupla2)

print("\nExemplo3 - Tupla")
tupla3 = (4)  # Isso não é uma tupla
print(type(tupla3))
print(tupla3)

print("\nExemplo4 - Tupla")
tupla4 = (4, )  # Isso é uma tupla
print(type(tupla4))
print(tupla4)

print("\nExemplo5 - Tupla")
tupla5 = (4, 5, )  # Isso é uma tupla
print(type(tupla5))
print(tupla5)

# Podemos gerar uma tupla dinamicamente com range
print("\nExemplo6 - Tupla")
tupla6 = tuple(range(11))
print(type(tupla6))
print(tupla6)

# Desempacotamento de tuplas
# OBS: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar
print("\nExemplo7 - Tupla")
tupla7 = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla7
print(escola)
print(curso)

# As tuplas são imultaveis, ou seja, não pode ser alterada. Não eh possivel inserir um novo elemento em uma
# tupla apos a sua criacao
print("\nExemplo8 - Tupla")
tupla8 = (1, 2, 3, 4, )

# Metodos para adicao ou remocao de elementos nao existem, visto que as tuplas são imultaveis

# Soma, Valor Maximo, Valor Minimo
# * Se os valores forem inteiros ou reais
print("\nExemplo9 - Tupla")
tupla9 = (1, 2, 3, 4, 5, 6, 0)
print(max(tupla9))
print(min(tupla9))
print(len(tupla9))
print(sum(tupla9))

# Concatenação de tuplas
print("\nConcatencanao")
tupla1 = 1, 2, 3,
print(tupla1)
tupla2 = 4, 5, 6,
print(tupla2)
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)
# Tuplas sao imultaveis
tupla3 = tupla1 + tupla2
print(tupla3)

# Verificar se um elemento esta na tupla
tupla3 = 1, 2, 3,
print(3 in tupla3)
print(33 in tupla3)

# Iterando sobre a tupla
tupla1 = (11, 12, 33)
for elemento in tupla1:
    print(elemento)

for indice, elemento in enumerate(tupla1):
    print(f'Indice {indice} e elemento {elemento}')

# Contando elementos dentro de uma tupla
print("\nContando elementos dentro de uma tupla")
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas
# Devemos usar tuplas sempre que nao precisar modificar os dados contidos em uma colecao

# Exemplo 1
meses_tupla = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
meses_lista = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']
print(meses_tupla)
print(len(meses_tupla))

# O acesso de elementos de uma tupla eh semelhante ao acesso em uma lista
print(meses_tupla[3:6])

# Iterar com while
i = 0
while i < len(meses_tupla):
    print(meses_tupla[i])
    i += 1

# Verificando em qual indice um elemento esta na tupla
print("\nVerificando em qual indice um elemento esta na tupla")
print(meses_tupla.index('Março'))
print(meses_tupla.index('Junho'))
print(dir(meses_tupla))
print(meses_tupla[0:])
print(meses_tupla[5:9])


# Porque utilizar tuplas

# 1 - Tuplas são mais rapidas que listas
# 2 - Tuplas deixam o código mais seguro (devido a imultabilidade)

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova_tupla = tupla
print(nova_tupla)

outra_tupla = 4, 5, 6,
nova_tupla = nova_tupla + outra_tupla
print(nova_tupla)
print(tupla)