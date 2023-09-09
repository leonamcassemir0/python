# Para criar uma função usamos def
"""
def my_function():
    soma = 0
    for x in range(0, 11):
        soma = soma + x
    return soma

print(my_function())
"""

# Podemos usar pass para passar a função sem ter código dentro dele
"""
def my_function():
    pass
"""

# Podemos ordenar os argumentos dessa forma:
"""
def my_function(a, b, c):
    print(a, b, c)

my_function(b="Leonam", a="Manoel", c="Yuri")
"""

# Usar *args permite adicionar vários parametros (cria uma tupla)
"""
def my_function(*dados):
    print(dados)

my_function("Leonam", "Yuri", "Manoel", "Eneia")
"""

# Usamos **kwargspara criar dicios
"""
def my_function(**dados):
    print(dados["filho1"])

my_function(filho1="Leonam", filho2="Yuri", pai="Manoel", mae="Eneia")
"""
