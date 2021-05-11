"""
Reduce

Para entender o reduce()

# Imagine que voce tem uma colecao de dados

dados = [a1, a2, a3, ..., an]

# E voce tem uma funcao que recebe DOIS parametros:

def funcao(x, y):
    return x * y

Assim como map() e filter, a funcao reduce recebe dois parametros: a funcao e o iteravel.

reduce(funcao, dados)

A funcao reduce(), funciona da seguinte forma:

- Passo 1: res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos do iteravel e guarda o resultado.
- Passo 2: res2 = f(res1, a3) # Aplica a funcao passando o resultado do passo 1 mais o terceiro elemento
e guarda o resultado.

Isso é repetido até o final.

- Passo 3: res3 = f(res2, a4)
  .
  .
  .
- Passo n: resn = f(resn-1, an)

Ou seja, em cada passo ela aplica a funcao passando como primeiro argumento o resultado da aplicacao anterior.
No final reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a funcao reduce() como:

funcao(funcao(funcao(funcao(a1, a2), a3),a4)...,an)
"""

# Como funciona na pratica


