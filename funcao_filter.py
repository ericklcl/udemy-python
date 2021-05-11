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
# print(paises)

res = filter(None, paises)
# print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
# print(list(res))

res = filter(lambda pais: pais != '', paises)
# print(list(res))

# Diferença entre map e filter:

# map() -> Recebe dois parametros, uma funcao e um iteravel e retorna um objeto mapeamento a funcao para cada
# elemento do iteravel

# filter() -> Recebe dois paramentros, uma funcao e um iteravel e retorna um objeto filtrando apenas os elementos
# de acordo com a funcao


# Exemplos mais complexos
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]
print(usuarios)
# Filtrar os usuarios que estao inativos no Twitter

# Forma 1
inativos = list(filter(lambda x: len(x['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda x: not x['tweets'], usuarios))
print(inativos)

# Combinar Filter e Map
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
print(list(map(lambda x: f"Sua instrutora eh {x}", filter(lambda nome: len(nome) < 5, nomes))))

