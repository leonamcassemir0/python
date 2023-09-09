numero = int(input("Digite o valor: "))

if numero > 0:
    if (numero % 2) == 0:
        print(f'{numero} eh PAR!')
    else:
        print(f'{numero} eh IMPAR!')
else:
    print('Nao ha divisao por 0 ou número negativos pares!')
