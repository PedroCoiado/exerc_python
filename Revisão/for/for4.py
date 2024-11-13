numeros = []
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
# Adicionar os numeros a lista
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)

maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print("o maior número é ",maior)

