# Primeiro cálculo de somas
"""
x = 40
y = 3 / x
c = 0
soma = 0

for t in range(1, 4):
    k = (32 + c) / (x - t)
    c += 1
    soma += k

soma += 340
soma += y
print(f"O resultado final eh {soma}")
"""

# Segundo cálculo de somas
"""
x = 480 / 2
y = 21
g = 480
soma = 0
for s in range(1, 21):
    soma += (g - 5) / (y + s)

soma += x
print(f"A soma eh igual a: {soma}")
"""

# Terceiro cálculo de somas
a = 23
b = 1 / 2
r = 1
j = 1
soma = 0
for x in range(1, 16):
    r *= 2
    soma += (r + j) / (a)
    a += 2
    j = (r + j)

soma += b
print(f"O resultado eh {soma}")
