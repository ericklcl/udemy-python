"""
Modulo Collectios - Deque

Podemos dizer que o deque é uma lista de alta performance
"""

# Importando
from collections import deque

deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')
print(deq)
deq.appendleft('y')
print(deq)

# Remover elementos no deque
print(deq.pop())
print(deq)
print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)
