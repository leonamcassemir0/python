chave = input('Digite a base da senha: ')
senha = ''

for letra in chave:
    if letra in 'Aa':
        senha = senha + '10'
    elif letra in 'Bb':
        senha = senha + '@'
    elif letra in 'Cc':
        senha = senha + '1'
    elif letra in 'Dd':
        senha = senha + '*'
    elif letra in 'Ee':
        senha = senha + '45'
    elif letra in 'Ff':
        senha = senha + '$'
    elif letra in 'Gg':
        senha = senha + '!'
    elif letra in 'Jj':
        senha = senha + '%'
    elif letra in 'Mm':
        senha = senha + '31'
    elif letra in 'Ss':
        senha = senha + '2'
    else:
        senha = senha + letra
print(senha)
