"""
Iterator ->
 - Um objeto que pode ser iterado;
 - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() é chamada;
Iterable ->
 - Um objeto que irá retornar um iterator quando a funcao iter() for chamada.
"""

nome = 'Geek'  # É um iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable mas não é um iterator.

print(nome)
print(numeros)

# print(next(nome))  # TypeError: 'str' object is not an iterator

it1 = iter(nome)
it2 = iter(numeros)

print(type(it1))

# Return the next item from the iterator. If default is given and the iterator
#     is exhausted, it is returned instead of raising StopIteration
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))

nome = 'Geek'

for letra in nome:
    print(f'{letra}')
