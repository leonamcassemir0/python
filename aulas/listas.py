"""
# LISTAS(Arrays)

# (index)    0      1   2     3   -> 4 elementos
lista1 = ['Leonam', 5, 2.4, True]
print(type(lista1))
print(lista1)
print(lista1[1])
# (index) 0  1  2  3  4  5  6  7  8  9  -> 10 elementos
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista2[-3])  # Negativo inverte a ordem do index

# END
lista3 = ["Leonam", "Uirley", "do", "Nascimento", "Cassemiro"]
print(lista3[0], end=lista3[4])

# SLICE
print(lista3[::])  # mesma coisa que print(lista2)
print(lista3[1:])  # começa no index 1 até o final da lista
print(lista3[:6])  # começa no index 0 até o index 6

# LEN (lenght)
lista4 = [1, False, "EU", 3, 2.75, 3.0]
print(len(lista4))

# Funções que funcionam somente com números (max,min,sum)
lista5 = [1, 2, 3, 4, 5]
print(sum(lista5))
print(max(lista5))
print(min(lista5))

# Transformar variaveis em listas
nome = "Leonam Cassemiro"
lista6 = list(nome)
num = range(10)
lista7 = list(num)
print(nome)
print(lista6)
print(num)
print(lista7)
"""

"""
lista = ["Leonam", "Cassemiro"]

# APPEND = Adiciona elementos ao final da lista
lista.append("Smart")
print(lista)

# INSERT = Adiciona o elemento no index indicado
lista.insert(1, "Lindo")
print(lista)

# EXTEND = Adiciona mais de um elementos na lista
lista.extend(["Uirley", "Nascimento"])
print(lista)

# POP = Remove o último elemento da lista
lista.pop()
print(lista)
lista.pop(2)
print(lista)

# REMOVE = Remove um elemento específico da lista
lista.remove("Lindo")
print(lista)

# DEL = Deleta a lista por completo
# CLEAR = Deleta os argumentos da lista, mas não a lista em si
lista.clear()
print(lista)
del lista
print(lista)
"""
