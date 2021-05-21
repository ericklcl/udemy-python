"""
Generators

Generators ocupam menos recursos em memoria que list/set comprenhensions

- Tuple Comprehension = Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# print([nome[0] == 'C' for nome in nomes])
# print(all([nome[0] == 'C' for nome in nomes]))
# print(any([nome[0] == 'C' for nome in nomes]))
# print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))  # Eh um tipo generator
print(res)

# Ao utilizar all e any é preferível utilizar generators.

# getsizeof - Return the size of object in bytes.
from sys import getsizeof

# print(getsizeof('Geek'))
# print(getsizeof('Geek University'))
# print(getsizeof(5))
# print(getsizeof(5.0))
# print(getsizeof(127))
# print(getsizeof(5356481122))
# print(getsizeof(True))

list_comp = getsizeof([x * 10 for x in range(1000)])
print(list_comp)
set_comp = getsizeof({x * 10 for x in range(1000)})
print(set_comp)
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(dict_comp)
gen = getsizeof(x * 10 for x in range(1000))
print(gen)

# Eu posso iterar no Generator Expression ? Sim.
print("\nIterando em um Generator")
gen = (x * 10 for x in range(1000))
print(type(gen))
print(gen)

for num in gen:
    print(num)
