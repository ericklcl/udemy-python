arquivo = open('texto.txt')

print(arquivo)

print(arquivo.read())

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parametro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek

print("### NOVA LEITURA ###")
arquivo.seek(0)

print(arquivo.read())

arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())
