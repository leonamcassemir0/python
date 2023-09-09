"""
# Módulo são arquivos em python, podendo fazer eles interagirem entre si.


# IMPORT importa outros módulos para o módulo atual

    import random
    print(random.random())


# FROM (módulo) IMPORT (função específico)

    from random import (
        random,
        choice
    )
    print(random())
    lista = ("pedra", "papel", "tesoura")
    print(choice(lista))


# IMPORT (módulo) AS (renomeie o módulo)

    import random as rd
    print(rd.random())
    from random import (
        random as rd,
        choice as ch
    )
    print(rd())
    lista = ("pedra", "papel", "tesoura")
    print(ch(lista))


# Podemos acessar outras pastas e importá-las:

    from outroModulo import outro
    print(soma(2, 3))


# .__doc__ pega a documentação do módulo (parte string)
    -> É mais comum usarmos o help no terminal para encontrar as
    características do módulo.

    import random
print(random.gauss.__doc__)
"""
