base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor da expoente: "))


def potenciacao(b, e):
    if b and e > 0:
        return f"potenciação da base {b} e expoente {e} eh igual a ", int(b**e)
    else:
        return "Não conseguimos calcular potenciação negativa!"


print(potenciacao(base, expoente))
