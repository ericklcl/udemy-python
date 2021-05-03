lista = [3, 4, 6, 7, 8]

print(list(map(lambda x: x ** 3, lista)))

cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27),
           ('Nova York', 28), ('Londres', 22)]

# temp_f = 9/5 * temp_c + 32

temp_c_f = lambda dados: (dados[0], 9 / 5 * dados[1] + 32)

print(cidades)
print(list(map(temp_c_f, cidades)))
