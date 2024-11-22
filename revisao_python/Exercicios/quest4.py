# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

# # if letra == "a" or "A":

# if letra == 'a' or letra == 'A':
#   print("É vogal")
# elif letra == 'e' or letra == 'E':
#   print("É vogal")
# elif letra == 'i' or letra == 'I':
#   print("É vogal")
# elif letra == 'o' or letra == 'O':
#   print("É vogal")
# elif letra == 'u' or letra == 'U':
#   print("É vogal")
# else:
#   print("É uma consoante!")


if letra in "aeiouAEIOU":
  print("é uma vogal.")
else:
  print("é uma consoante.")

# letra = letra.lower()

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("A letra é vogal")
# else:
#     print("A letra é consoante")
