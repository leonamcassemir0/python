x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))


def media(a, b):
    if a and b > 0:
        return int(a+b/2)


print(media(x, y))
