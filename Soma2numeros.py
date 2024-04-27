#Python 3.6
#coding utf-8
#soma de dois numeros
#Escopo global, Local e da Função
n1 = int(input("qual valor do v1: "))
n2 = int(input("E o v2: "))

def var1(A):
    var2(A)

def var2(b):
    global x
    x = 500
    print(f"A soma de var1 e var2: {n2+b}")
    print(x)

var1(n1)
print(x)


###############################


def primeira_funcao():
    # Defina duas variáveis
    a = 10
    b = 20
    # Chame a segunda função
    segunda_funcao(a, b)

def segunda_funcao(x, y):
    # Some as variáveis x e y
    resultado = x + y
    # Printe o resultado
    print(f"A soma de {x} e {y} é igual a {resultado}")

# Chame a primeira função para iniciar o processo
primeira_funcao()