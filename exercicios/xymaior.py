x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))


def maior(a, b):
    if a > b:
        return "X é maior que Y"
    else:
        return "Y é maior que X"


print(maior(x, y))
