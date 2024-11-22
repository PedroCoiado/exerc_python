# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o seu sexo (F ou M): ") 

# F = "Feminino"
# M = "Masculino"

if sexo == "F" or sexo == "f":
    print("seu sexo é Feminino")
elif sexo == "M" or sexo == "m":
    print("Seu sexo é Masculino")
else:
    print("Sexo inválido")

# O comando lower() converte as letras para minúsculas
# O comando upper() converte as letras para maiúsculas

# sexo = sexo.lower()
# if sexo == "f":
#     print("Feminino")
# elif sexo == "m":
#     print("Masculino")
# else:
#     print("Sexo inválido")
