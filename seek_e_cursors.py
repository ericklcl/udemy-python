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

arquivo.seek(0)
ret = arquivo.readline()

print(type(ret))
print(ret)
print(ret.split(" "))

print([len(palavra) for palavra in ret.split(" ")])

arquivo = open('texto.txt')
print(len(arquivo.readlines()))
