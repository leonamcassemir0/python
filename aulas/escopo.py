#Escopo global e local
x = 5

def function():
    x = 3
    print('O dado da variavel local: ', x)

function()
print('O dado da variavel global: ', x)

#Para tornar o código legível, costuma colocar o nome da variável com o tipo de dado que preencherá ela.