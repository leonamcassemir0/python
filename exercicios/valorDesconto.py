print("Calcular valor com desconto!")

valor = float(input("Digite o valor: R$ "))
desconto = float(input("Qual será o desconto? "))

valor_final = valor - ((valor * desconto) / 100)
print(f"O valor final com desconto e: R$ {round(valor_final, 2)}")
