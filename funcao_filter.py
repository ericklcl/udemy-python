"""
Filter

filter() - serve para filtrar dados de uma determinada colecao

Return an iterator yielding those items of iterable for which function(item) is true.
If function is None, return the items that are true.
"""
import statistics

'''
valores = 1, 2, 3, 4, 5, 6
print(valores)

media = sum(valores) / len(valores)
print(media)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a funcao mean
media = statistics.mean(dados)

# OBS 01: Asssim como a função map(), a função filter recebe dois parametros, sendo:
# uma função e um iterável
# OBS 02: Asssim como a função map(), após serem utilizados os dados de filter() eles são excluídos da memória

print(media)
res = filter(lambda x: x > media, dados)
print(list(res))

'''

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

