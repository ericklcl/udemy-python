"""
O que são decorators:
- Decorators são funcoes
- Decorators envolvem outras funcoes e aprimoram seus comportamentos
- Decorators também são exemplos de Higher Order Functions
- Decorators tem uma sintaxe própria, usando "@" (Syntax Sugar)
"""


# Decorators como funções - Sintaxe não recomendada

def seja_educado(funcao):  # Geralmente uma funcao decorator recebe como parametro uma funcao
    def sendo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um otimo dia')

    return sendo  # Retorna a funcao e não a execucao da funcao


def saudacao():
    print('Seja bem-vindo(a) a Geek University')


# Testando 1

# saudacao()
# teste = seja_educado(saudacao)
# teste()


# Testando 2

def raiva():
    print('Eu te odeio')


# raiva_educada = seja_educado(raiva)
# raiva_educada()


# Decorators como funções - Sintaxe recomendada

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome eh Pedro')


# Testando
apresentando()
