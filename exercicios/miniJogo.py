import random

print('Tente acertar o numero!')
num = int(input('Até que número você quer que sorteie? '))
numero = random.randrange(num)

while num != numero:
    escolha = int(input('Qual o numero? '))
    if escolha == numero:
        print('Parabens voce acertou!')
        break
    elif escolha > num:
        print('Numero inserido maior que o numero limite do sorteio feito!')
