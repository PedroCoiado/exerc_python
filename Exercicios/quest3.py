# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite a sigla do seu gênero (F ou M):") 

# F = "Feminino"
# M = "Masculino"

if sexo == "F" or sexo == "f":
    print("seu sexo é Feminino")
elif sexo == "M" or sexo == "m":
    print("Seu sexo é Masculino")
else:
    print("Sexo inválido")
