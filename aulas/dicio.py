# São coleções não ordenadas, mutáveis e que NÃO permite valores duplicados.

"""
dicio = {"chave1": "Leonam", "chave2": 13, "chave3": False}
print(dicio)
print(dicio["chave1"])
print(dicio.get("chave2"))
print(type(dicio))
"""

dicio2 = {
    "nome": "Leonam",
    "idade": 21,
    "nacionalidade": "Brasileiro",
    "estado": "MG"
}

# VALUES = Pega todos os valores
print(dicio2.values())

# ITEMS = Cria tuplas com a chave e o valor
print(dicio2.items())

# UPDATE = Atualiza uma chave com um novo valor
dicio2.update({"nome": "Yuri"})
print(dicio2)

# POPITEM = Remove o último valor
dicio2.popitem()
print(dicio2)

dicio3 = ["Leonam", 21, "Yuri", 25, "Luna", 5, "Manoel", 65]
print(dicio3)
print(type(dicio3))
dicio4 = dict(dicio3).fromkeys(dicio3)
print(dicio3)
print(type(dicio3))
