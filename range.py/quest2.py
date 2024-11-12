# 2.Faça um programa que leia 5 números e informe a soma e a média dos números.


#justificar que a soma de todos os numeros tem a base de começar pelo numero neutro
# em situação de multiplicação e divisão, tendo assim uma forma mais concreta de chegar
# no valor real.
soma = 0
for x in range(5):
  numero = float(input(f"Digite o {i+1}º número: "))
  # Comando em dicionario, aplica a uma sequencia de numeros sequenciais, (variavel + 1)
  # Seignificando que vai começar pelo numero "1"
  soma += numero

media = soma / 5

print("A soma dos números é: ", soma)
print("A média dos números é: ", media)