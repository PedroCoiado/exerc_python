def soma(n1,n2):
    return n1 + n2

def produto(n1,n2):
    return n1 * n2

def restoDivisao(n1, n2):
    return n1 % n2

def separarResultados(texto):
    print("----------------- O resultado de "+texto+"-------------------")

print("Olá, seja bem-vindo ao programa de calculos")
separarResultados("Soma")
print(" o resultado da soma entre os numeros 5 e 10 é:"+str(soma(5,10)))
separarResultados("multiplicação")
print("Entre os números 5 e 10 é "+str(produto(5,10)))
separarResultados("Divisão")
print("Entre os numeros 5 e 10 é "+str(restoDivisao(5,10)))