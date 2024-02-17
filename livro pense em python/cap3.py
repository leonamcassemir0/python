# palavra printada com 70 espaços
"""
def right_justify(s):
    print(70*" ", s)


right_justify('monty')
"""


"""
def do_twice(f, s):
    f(s)
    f(s)


def print_twice(s):
    print(s)
    print(s)


def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)


do_twice(print, 'spam')
do_four(print, 'leonam')
"""


def do_twice():
    for i in range(2):
        for i in range(2):
            print('+', end=' ')
            print(4*'-', end=' ')
            print(4*" ", )
        print('+')
        for i in range(4):
            print('|', 4*" ")
    for i in range(2):
        print('+', end=' ')
        print(4*'-', end=' ')
    print('+')


do_twice()