# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sigla = input("Digite a sigla do seu gênero (F ou M):") 

F = "Feminino"
M = "Masculino"

if sigla == "F":
    print("seu genero é Feminino")
elif sigla == "M":
    print("Seu genero é Masculino")
else:
    print("Sexo inválido")