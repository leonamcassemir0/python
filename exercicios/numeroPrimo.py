numero = int(input('Qual o numero? '))

if numero > 1:
    for x in range(2, numero):
        if (numero % x) == 0:
            print('Esse nao eh primo')
            break
        else:
            print('Esse eh primo')
            break
else:
    print('Numero igual ou menor que 0!')
