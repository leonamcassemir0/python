print("Qual a situacao sobre sua idade?")

idade = input("Digite sua idade: ")
idade = int(idade)

if idade < 16:
    print("Voce eh MENOR!")
elif idade >= 16 and idade < 18:
    print("Voce eh EMANCIPADO!")
elif idade >= 18:
    print("Voce eh MAIOR!")
