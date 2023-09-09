y = 0

for x in range(1, 6):
    x = int(input(f"Digite o {x} valor: "))
    if x > y:
        maior = x
    y = x

print(f"O maior numero eh {maior}")
