numero = int(input('Digite o numero que deseja fatorar: '))
fat = 1


if numero < 0:
    print('Nao existe fatorial para numero negativo')
elif numero == 0:
    print('O fatorial de 0 eh 0!')
else:
    for x in range(1, numero + 1):
        fat = fat * x
        print(f'O fatorial de {numero} eh {fat}')
