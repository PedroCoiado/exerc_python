# Programa Python simples para entender a instrução elif  
nota = int(input("Digite a nota?"))
# Aqui, estamos pegando uma marca inteira e recebendo a entrada dinamicamente  
if nota > 85 and nota <= 100:
# Aqui, estamos verificando a condição. Se a condição for verdadeira, entraremos no bloco    
    print("Parabéns! Você tirou nota A...")
elif nota > 60 and nota <= 85:
# Aqui, estamos verificando a condição. Se a condição for verdadeira, entraremos no bloco  
    print("Você tirou nota B+...")
elif nota > 40 and nota <= 60:
# Aqui, estamos verificando a condição. Se a condição for verdadeira, entraremos no bloco    
    print("Você tirou nota B...")
elif (nota > 30 and nota <= 40):
# Aqui, estamos verificando a condição. Se a condição for verdadeira, entraremos no bloco  
    print("Você tirou nota C...")
else:
    print("Você está reprovado")
