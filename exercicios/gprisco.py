import os

name = input("Digite seu nome: ")


def cpf():
    cpf = input("Digite seu CPF: ")


cpf()
if len(cpf) == 11:
        return cpf2
    else:
        return cpf()
rg = int(input("Digite seu rg: "))
nasc = str(input("Digite sua data de nascimento(dd/mm/yyyy): "))

listaAno = nasc.split("/")
idade = 2023 - int(listaAno[2])
print(idade)
