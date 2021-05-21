"""
zip() -> Cria um iterável (zip object) que agrega elemento de cada um dos iteraveis passados como entrada em pares.
"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))
print(list(zip1))
print(set(zip1))
print(dict(zip1))
