"""
StringIO

ATENCAO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa
ter permissao:
    - Permissao de leitura -> Para ler o arquivo
    - Permissao de escrita -> Para escrever o arquivo

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import

from io import StringIO
import os

mensagem = "Esta é apenas uma string normal\n"

# Podemos criar um arquivo em memoria já com uma string inserida ou mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)

# Agora tendo o arquivo, podemos utilizar tudo que sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write("Outro texto")

# Movimentando o cursor
arquivo.seek(0)
print(arquivo.read())

print(os.getcwd())
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretorio eh absoluto ou relativo
print(os.path.isabs('/home/elima/'))
print(os.uname())

# OBS para usuários windows
# Se voce infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretório.

print(os.listdir("/etc"))

