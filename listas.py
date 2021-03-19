print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Nao encontrei o número {num}')

# Sort - The sort() method sorts the elements of a given list in a specific ascending or descending order.
# Syntax - list.sort(key=..., reverse=...)
print("\n### Testando o metodo sort ###")
print("Ordenando a lista")
lista1.sort()
print(lista1)
lista1.sort(reverse=True)
print(lista1)

# Count - The count() method returns the number of times the specified element appears in the list.
# Syntax - list.count(element)
print("\n### Testando o metodo count ###")
print(lista1.count(1))
print(lista2.count('e'))

# Append - The append() method adds an item to the end of the list.
# Syntax - list.append(item)
print("\n### Testando o metodo append ###")
print(lista1)
lista1.append(999)
print(lista1)

lista1.append([8, 3, 1])
print(lista1)

if [22, 27, 27] in lista1:
    print("Encontrei a lista")
else:
    print("Nao encontrei a lista")

# Extend - The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# Syntax - list.extend(iterable)
print("\n### Testando o metodo extend ###")
lista1.extend([123, 44, 67])
print(lista1)
lista1.extend("Geek")
print(lista1)

# Insert - The list insert() method inserts an element to the list at the specified index.
# Syntax - list.insert(i, elem)
print("\n### Testando o metodo insert ###")
print(lista1)
lista1.insert(2, "Novo Valor")
print(lista1)

# Juntando duas listas
print("\n### Juntando duas listas ###")
lista6 = lista1 + lista2
print(lista1)
print(lista2)
print(lista6)
lista1.extend(lista2)
print(lista1)

print("\n")
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista1)
print(lista2)

# Reverse - The reverse() method reverses the elements of the list.
# Syntax - list.reverse()
print("\n### Testando o metodo reverse ###")
print(lista1)
print(lista2)
print("\n")
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
print("\nOutra forma de inverter a lista - usando slice")
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista1[::-1])
print(lista2[::-1])

print("\nCopiar uma lista")
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista6 = lista2.copy()
print(lista6)

# len - The len() function returns the number of items (length) in an object.
# Syntax - len(s)
# s - a sequence (string, bytes, tuple, list, or range) or a collection (dictionary, set or frozen set)
print("\nUsando o metodo len para verificar o tamanho de uma lista (numero de elementos)")
print(len(lista6))

# pop - The pop() method removes the item at the given index from the list and returns the removed item.
# The pop() method returns the item present at the given index. This item is also removed from the list.
# Syntax - list.pop(index) - The argument passed to the method is optional. If not passed,
# the default index -1 is passed as an argument (index of the last item).
print("\nRemovendo o elemento de uma lista")
print(lista5)
print(f"Item removido: {lista5.pop()}")
print(lista5)
print(f"Item removido: {lista5.pop(2)}")
print(lista5)

# clear - The clear() method removes all items from the list.
# Syntax - list.clear()
# removendo todos os elementos da lista
print("\nLimpando a lista inteira")
print(lista5)
lista5.clear()
print(lista5)

# repetir elementos através do simbolo de multiplicacao
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# split - The split() method breaks up a string at the specified separator and returns a list of strings.
# Syntax - str.split([separator [, maxsplit]]).
# If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
print("\nTransformando uma string em uma lista")
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# join - The join() string method returns a string by joining all the elements of an iterable, separated by a string
# separator.
# Syntax - string.join(iterable)
# The join() method provides a flexible way to create strings from iterable objects. It joins each element of an
# iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called)
# and returns the concatenated string.
print("\nTransformando uma lista em uma string")
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
curso = ' '.join(lista6)
print(curso)

type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# Iterando sobre listas

# Exemplo 1 - Utilizando o for
soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 - Utilizando o while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = 'sair'
    if produto != 'sair':
        carrinho.append(produto)

print("### Imprimindo os produtos ###")
for produto in carrinho:
    print(produto)

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)
print(numeros[2])
print(numeros[-2])

#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[3])
print(cores[-2])

# loop utilizando for
print('\n# loop utilizando for #')
for cor in cores:
    print(cor)

# loop utilizando while
print('\n# loop utilizando while #')
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

print('\nEntendendo o enumerate')
for indice, cor in enumerate(cores):
    print(indice, cor)

cores = list(enumerate(cores))
print(cores)

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# Outros metodos não tão importantes entretanto uteis
print('\n# Encontrando um indice em uma lista #')
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(6))
print(numeros.index(9))
# exibindo o erro
try:
    print(numeros.index(33))
except ValueError:
    print('Numero nao existe na lista')
print(numeros.index(5, 1))  # buscando a partir do indice 1
print(numeros.index(5, 2))  # buscando a partir do indice 2
print(numeros.index(5, 3))  # buscando a partir do indice 3
# print(numeros.index(5, 4))  # buscando a partir do indice 4

# Podemos fazer busca dentro de um range, inicio/fim
print("\nPodemos fazer busca dentro de um range, inicio/fim")
print(numeros.index(8, 3, 6))  # Buscar o valor 8 entre os indices 3 a 6

# Revisando o slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de listas
print("\nTrabalhando com slice de listas")
lista = [1, 2, 3, 4]
print(lista[::])
print(lista[1:])
print(lista[1])
print(lista[-1])
print(lista[-2])
print(lista[:2])
print(lista[:4])
print(lista[1:3])
print(lista[:-1])  # comecando no indice 0 e pegando até o penultimo indice
print(lista[1::2])
print(lista[::2])
print(lista[1::-1])
nome = 'Programacao em Python: Essencial'
print(nome[::-1])

# Invertendo valores em uma lista
nomes = ['Geek', 'University']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

# Soma, Valor Máximo, Valor Mínimo, Tamanho de uma lista
lista = [1, 2, 3, 4, 5, 6]
print(f'Soma: {sum(lista)}')  # Soma
print(f'Maximo: {max(lista)}')  # Maximo
print(f'Minimo: {min(lista)}')  # Minimo
print(f'Tamanho: {len(lista)}')  # Tamanho

# Transformar uma lista em uma tupla
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
