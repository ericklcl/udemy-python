"""
Poderiamos chamar esse parametro de **xis, mas por convencao chamamos de **kwargs

Este eh so mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parametors nomeados, e transforma esses
parametros extras em um dicionario.
"""


# Exemplo

def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


def cores_favoritas(a, b, c, **kwargs):
    print(kwargs)


cores_favoritas(1, 2, 3, marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} eh {cor}.')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: Os parametros *args e **kwargs nao sao obrigatorios

cores_favoritas()
cores_favoritas(nome='joao')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'Voce recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Nao tenho certeza quem voce eh"


print("\nExemplo 2")
print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))


# Nas nossas funcoes podemos ter (NESTA ORDEM):

# - Parametros obrigatorios;
# - *args;
# - Parametros default (nao obrigatorios)
# - **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(25, 'Julia')
minha_funcao(18, 'Felicity', 453, solteiro=True)
minha_funcao(34, 'Felipe', eu='Nao', voce='vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entenda por que eh importante manter a ordem dos parametros na declaracao

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


"""
a = 1
b = 2,
instrutor = 3
args = (4,)
kwargs = {sobrenome='university', cargo='instrutor'}
"""
print(mostra_info(1, 2, 3, 4, sobrenome='University', cargo='Instrutor'))


# Desempacotar com kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

# Os nomes da chave em um dicionario devem ser os mesmos dos parametros da funcao
dicionario = dict(a=1, b=2, c=3)


def soma(a, b, c):
    print(a + b + c)


soma(**dicionario)

# Se os nomes das chaves dos dicionarios forem diferentes do parametro da funcao sera gerado um TypeError.
