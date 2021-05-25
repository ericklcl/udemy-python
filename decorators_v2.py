# Decorators

def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)

    return inner_function()  # Retorna o resultado da funcao


outer_function()
