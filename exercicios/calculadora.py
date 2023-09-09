"""
Calculadora python usando os conhecimentos aprendidos até agora.

Siga o passo-a-passo explicando:

1. Defini uma função (def calculadora())
    -> Logo abaixo fiz a introdução do programa colocando todas as
    informações e operações disponíveis em uma calculadora convencional.
    atribuindo número para cada operação.
    -> Criei uma variavel(escolha) onde a pessoa digita
    o número referente a operação desejada.

2. Após introduzir o programa fiz vários if´s onde faço as operações
    -> Criei uma variavel(valor) nova onde defino um float
    onde o usuário digita o valor númerico que quer saber.
    -> Onde é necessário dois valores criei duas variaveis(valor1 e valor2).
    -> O resultado atribui em prints.
        - Não usei return porque a função "acaba" quando usamos return e
        temos que fazer com que ele chegue até o final.

3. Depois criei outra variável(escolha2) onde atribui uma str(string)
em que a pessoa responde com s(sim) ou n(não) se deseja continuar
fazendo outra operação.
    -> Aqui utilizamos outro if somente para a resposta s(sim),
    fazendo um return da própria função(calculadora()).
    repetindo todo o processo.
    -> Em caso de resposta diferente de s ou S(ambos sim)
    paramos a função e seguimos o código normalmente.

4. Encerrado a função crio o restante do código:
    -> Faço uma chamada na função(calculadora()) para que rode ela.
    -> Depois crio um print("JOGO TERMINADO") onde encerra o programa.
    pois o usuário digitou n ou N(ambos não) na variável escolha2
    onde não quis fazer outra operação.
"""


def calculadora():
    print("CALCULADORA PYTHON")
    print("-"*15)
    print("Qual operação você deseja realizar")
    print("1. Porcentagem (%)")
    print("2. Divisão invertida (1/x)")
    print("3. Potenciação quadrática (x^2)")
    print("4. Raiz quadrada (x^1/2)")
    print("5. Divisão (/)")
    print("6. Multiplicação (*)")
    print("7. Diminuição (-)")
    print("8. Adição (+)")
    escolha = int(input("Escolha sua operação: "))
    print("-"*15)

    if escolha == 1:
        valor = float(input("Digite o valor: "))
        porcentagem = float(
            input("Qual a porcentagem desejada (somente o valor)? "))
        print(valor * (porcentagem/100))
    elif escolha == 2:
        valor = float(input("Digite o valor: "))
        print(1/valor)
    elif escolha == 3:
        valor = float(input("Digite o valor: "))
        print(valor**2)
    elif escolha == 4:
        valor = float(input("Digite o valor: "))
        print(valor**(1/2))
    elif escolha == 5:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(valor1/valor2)
    elif escolha == 6:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(valor1*valor2)
    elif escolha == 7:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(valor1-valor2)
    elif escolha == 8:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(valor1+valor2)

    print("-"*15)
    escolha2 = str(input("Deseja fazer outra operação? (s/n) "))
    if escolha2 == "s" or escolha2 == "S":
        return calculadora()


calculadora()
print("-"*15)
print("JOGO TERMINADO")
