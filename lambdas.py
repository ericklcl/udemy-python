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

print(nome_completo(' erick ', 'LIMA     '))

amar = lambda: 'Como não amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x) / (1 / y) / (1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(4, 5, 6))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Oston Scort Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(autores)
autores.sort(key=lambda x: x.split(" ")[-1].lower())
print(autores)


def func_quad(a, b, c):
    """
    Retorna a funcao f(x) = a*x **2 + b * x + c
    """
    return lambda x: a * x ** 2 + b * x + c


teste = func_quad(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
