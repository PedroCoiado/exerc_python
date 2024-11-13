vogal = ["a","e","i","o","u"]
letra = input("Digite uma letra: ")
letra = letra.lower()
for v in vogal:
     if letra == v:
        print("A letra digitada é uma vogal")
# break tem a função de quebrar o código, o seja para ele parar no ponto emitido,
# então "a" é primeira letra a qual o usuário vai digitar, o programa localiza dentro "v"(vogal)
# executa "a" e fecha o programa, para ele não ficar sobrecarregando o sistema e a memória da aplicação
# mesma coisa com qualquer tipo de letra selecionada, dentro de vogal, caso não esteja dentro da lista vogal
# o comando entenderá que não é uma vogal. 
        break
else:
        print("A letra digitada não é uma vogal")