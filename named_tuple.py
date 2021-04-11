"""
Modulos collection - Named tuple
"""

tupla = (1, 2, 2, 3)
print(tupla)
print(tupla[1])

# Named Tuple -> Sao tuplas diferenciadas, onde especificamos um nome para a mesma e também parametros

# Importando
from collections import namedtuple

# Apos o import, precisamos definir o nome e parametros.

# Forma 1 - Declaracao Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaracao Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaracao Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=2, raca='chow chow', nome='ray')
print(ray)

print(ray[2]) # nome
print(ray.idade) # idade
print(ray.raca)

print(ray.index('chow chow'))
print(ray.count('chow chow'))




