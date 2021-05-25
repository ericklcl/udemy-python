# Closures

"""
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()
print(my_func)
print(my_func.__name__)
my_func()
my_func()
my_func()
"""

"""
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func('hi')
hello_func = outer_func('hello')

print(hi_func.__name__)
print(hi_func.__dir__)
hi_func()
"""

import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            f'Running "{func.__name__}" with arguments {args}'
        )
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


add_logger = logger(add)
add_logger(3, 4)
