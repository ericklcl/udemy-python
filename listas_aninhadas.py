"""
Listas Aninhadas

-
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)
[[print(valor) for valor in lista] for lista in listas]

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
