# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
  maior = num1
elif num2 > num1 and num2 > num3:
  maior = num2
else:
  maior = num3

print("O maior número é:", maior)