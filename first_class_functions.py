def square(x):
    return x * x


"""
=== PARTE 1

f = square(5)

print(square)
print(f)

g = square

print(square)
print(g)
print(g(5))
"""

########################################################

"""
=== PARTE 2
def cube(x):
    return x * x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)
"""

########################################################

"""
=== PARTE 3
def logger(msg):
    def log_message():
        print(f'Log: {msg}')

    return log_message


log_hi = logger('Hi')
log_hi()
"""


########################################################

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text


print_h1 = html_tag('h1')
print(html_tag)

print(print_h1)
print_h1('Teste Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test paragraph')
