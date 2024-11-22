# Primeiro exercício
def soma(a,b):
    return a+b

# Segundo exercício

def temperatura(Celsius, fracao, num):
    Fahrenheit = (Celsius * fracao) + num
    return Fahrenheit

# Terceiro exercício
def par_ou_impar(numero):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
# resultado = par_ou_impar(numero)
# print(f"{numero} é {resultado}")


# Quarto exercício

def palavra(texto):
    palavra_invertida = ""
    for i in range(len(texto) -1, -1, -1):
        """
        len(texto) - 1: A função len(texto) retorna o comprimento da string texto. 
        Subtrair 1 nos dá o índice do último caractere da string (lembre-se que os índices em Python começam em 0).

        -1: Este é o número final da sequência, mas ele é exclusivo. 
        Isso significa que a sequência vai até antes de -1, ou seja, até 0.

        -1: O passo é -1, indicando que a sequência deve ser gerada de trás para frente (decrescente).

        """        
        palavra_invertida += texto[i]
    return palavra_invertida

texto = input()
palavra_invertida = palavra(texto)
print(f"Palavra original: {texto}")
print(f"Palavra invertida: {palavra_invertida}")


# Quinto exercicio
def palindromo(palavra=""):

  palavra_invertida = palavra
  if palavra == palavra_invertida(palindromo):
    return "é um palíndromo!"
  else:
    return "não é um palíndromo."


# Sexto Exercicio

  
