# Primeiro exercicio
def soma(num1, num2):
    return num1 + num2

# Segundo exercicio
def converterCelFah(tempCelsius):
    fah = 1.8 * tempCelsius + 32
    return fah

# Terceiro Exercicio
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
# Quarto Exercicio

def inverter(texto):
    tam = len(texto)
    txt_invertido=("")
    for i in range(tam-1,-1,-1):
        txt_invertido += texto[i]
    return txt_invertido
    
# Quinto Exercicio
def palindromo(palavra):
    cp_palavra = palavra
    if cp_palavra==inverter(palavra):
        return "É um palindromo"
    else:
        return "Não é um palindromo"
    
# Sexto exercicio 
def media(lista_numeros):
    resultado = 0
    for i in lista_numeros:
        resultado += i
    return resultado / len(lista_numeros)

# Sétimo exercício
def lista_pares(lista_numeros):
    lst_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lst_pares.append(i)
    return lst_pares