"""
São funcoes sem nome, ou seja, funcoes anonimas.
"""


def funcao(x):
    return 3 * x + 1


print(funcao(7))

# Exemplo de expressao lambda

calc = lambda x: 3 * x + 1
print(calc(7))

nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()

print(nome_completo(' Erick ', 'Lima     '))
