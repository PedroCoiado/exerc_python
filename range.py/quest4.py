# 4 Faça um programa que leia 5 números e informe o maior número.

maior_num = int(input("Digite o 1º número: "))

for x in range(4):
  num = int(input(f"Digite Digite o {x+2}º número: "))
  if num > maior_num:
    maior_num = num

print("O maior número digitado foi: ",maior_num)
