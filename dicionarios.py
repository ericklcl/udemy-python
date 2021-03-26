"""
Dicionarios sao colecoes do tipo chave/valor

Dicionarios sao representados por chaves {}.
"""

print(type({}))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Criação de dicionarios

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

# Acessando elementos em um dicionario

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print("\nForma 1 - Acessando via chave, da mesma forma que lista/tupla")
print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get - Recomendada
print("\nForma 2 - Acessando via get - Recomendada")
print(paises.get('br'))
print(paises.get('ru'))

russia = paises.get('ru')

pais = paises.get('py')
if pais:
    print(f'Encontrei o pais {pais}'.format(pais=pais))
else:
    print(f'Nao encontrei o pais {pais}')

# Eh possivel definir um valor padrao para o dicionario usando o get, caso nao encontremos o objeto com a chave
# informada

pais = paises.get('ru', 'Nao encontrado')
print(f'Encontrei o pais {pais}'.format(pais=pais))

pais = paises.get('py', 'Nao encontrado')
print(f'Encontrei o pais {pais}'.format(pais=pais))

# Caso o get nao encontre o objeto com a chave informada, será retornado o valor None e não será gerado KeyError

# Podemos verificar se determinada chave se encontra em um dicionario
print("\n### verificando se a chave existe no dicionario ###")
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises.get('ru')
print(russia)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionario como chaves de dicionarios.
# Tuplas são bastante interessantes de serem utilizadas como chave de dicionario, pois as mesmas são imultaveis.
localidades = {
    (35.6895, 39.6917) : 'Escritorio em Tokio',
    (40.7128, 74.0060) : 'Escritorio em Nova York',
    (35.6895, 122.4194) : 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionario
print("\n ### Adicionar elementos em um dicionario ###")
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 (mais comum)
print('\nForma 1 - Adicionar elementos em um dicionario')
receita['abr'] = 350
print(receita)

# Forma 2
print('\nForma 2 - Adicionar elementos em um dicionario')
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1
print("\n### Atualizando dados em um dicionario - Forma 1 ###")
print(receita)
receita['mai'] = 550
print(receita)

# Forma 2
print("\n### Atualizando dados em um dicionario - Forma 2 ###")
receita.update({'mai':600})
print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario eh a mesma
# CONCLUSAO 2: Em dicionarios, NAO podemos ter chaves repetidas

# Remover dados de um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 - Mais comum
print("\n### Forma 1 ###")
print(receita)
ret = receita.pop('mar')
print(ret)
print(receita)


# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado.

# Forma 2
print("\n### Forma 2 ###")
print(receita)
del receita['fev']
print(receita)

# del receita['fev'] # Sera gerado um key error

# Se a chave não existir será gerado um key error
# Neste caso, o valor removido não é retornado.

# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
      - nome;
      - quantidade;
      - preço;
    Produto 2:
      - nome;
      - quantidade;
      - preço;
"""

# Opçao 1 - Lista

print("\n# Opcao 1 - Lista #")
carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber qual eh o indice de cada informacao no produto.

# Opcao 2 - Tupla

print("\n# Opcao 2 - Tupla #")
produto1 = 'Playstation 4', 1, 2300.00
produto2 = 'God of War 4', 1, 150.00
carrinho = (produto1, produto2)
print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto.

print("\n# Opcao 3 - Dicionario #")
# Opcao 3 - Dicionario
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informacao

# Metodos de dicionarios

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)
d.clear()
print(d)

# Copiando um dicionario para outro
d = dict(a=1, b=2, c=3)
# Forma 1
novo = d.copy() # deep copy
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2
d = dict(a=1, b=2, c=3)
novo = d
print(novo)
novo['d'] = 4
print(novo)
print(d)

# Forma não usual de criacao de dicionarios
print("\n# Forma não usual de criacao de dicionarios")
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# o metodo fromkeys recebe dois parametros: um iteravel e um valor
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
# em dicionarios python não pode haver repeticao de chave, por isso o segundo t e o segundo e nao foi acrescido.

veja = {}.fromkeys(range(1, 11), 'teste')
print(veja)