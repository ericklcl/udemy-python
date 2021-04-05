"""
Modulo collections - Default Dict

"""

dicionario = {'curso': 'Programacao em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

# print(dicionario['outro']) # ??? KeyError

# Ao criar um dicionario utilizando o default dict, nos informamos um valor default,
# podendo utilizar um lambda para isso. Esse valor sera utilizado sempre que nao houver um valor definido.
# Caso tentemos acessar uma chave que nao existe, essa chave será criada e o valor será atribuido.

# lambda sao funcoes sem nome que podem ou nao receber parametros de entrada e retornar valores

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programacao em Python Essencial'
print(dicionario)

print(dicionario['outro'])

print(dicionario)


