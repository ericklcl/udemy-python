"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

Return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True.
"""

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros ?
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros ?
print(all([]))  # Todos os números são verdadeiros ?
print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros ? Tupla
print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros ? Set
print(all('Geek'))  # Todos os números são verdadeiros ? String

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']

print(nomes)
print([nome[0] == 'C' for nome in nomes])
print(all([nome[0] == 'C' for nome in nomes]))

print([letra in 'eio' for letra in 'aeiou'])
print(all([letra in 'eio' for letra in 'aeiou']))

print(bool([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))

"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna Falso.

Return True if bool(x) is True for any x in the iterable. If the iterable is empty, return False.
"""

print('\nEstudo do Any')
print([0, 1, 2, 3, 4, 5])
print(any([0, 1, 2, 3, 4, 5]))  # Retorna True

print(any([0, '', False, '', 0, False]))  # Retorna False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [2, 4, 6, 8, 9] if num % 2 == 0]))

# Diferença entre all e any
# All retorna True se todos os elementos do iterável retornarem True e
# Any retorna True se ao menos 1 elemento do iterável retornar True
