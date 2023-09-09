# SETS são coleções não ordenadas, imutáveis e que não permite valores duplicados.
# Conhecido como conjuntos

"""
conjunto = {"item1", "item2", "item3", "item4", "item5"}
print(conjunto)
print(type(conjunto))
"""

"""
# Função set() permite transformar um dado em set
tupla = ("item1", "item2", "item3", "item4", "item5")
print(type(tupla))
print(tupla)
conjunto = set(tupla)
print(type(conjunto))
print(conjunto)
"""

"""
# Para acessar usamos laços de repetição ou de atribuição(in ou not in)
conjunto = {"item1", "item2", "item3", "item4", "item5"}
for x in conjunto:
    print(x)
print("item3" in conjunto)
"""

"""
# UNION é usada para unir dois conjuntos numa variável
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9, 10}
conjunto = conjunto1.union(conjunto2)
print(conjunto)
"""

"""
# INTERSECTION é usada para pegar valores em comum
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 3, 8, 1, 10}
conjunto = conjunto1.intersection(conjunto2)
print(conjunto)
"""

"""
# INTERSECTION_UPDATE é usada para achar valores em comum sem precisar estar numa variavel
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 3, 8, 1, 10}
conjunto1.intersection_update(conjunto2)
print(conjunto1)
"""

"""
# UPDATE é usada para unir dois conjuntos sem precisar de variavel
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9, 10}
conjunto1.update(conjunto2)
print(conjunto1)
"""
