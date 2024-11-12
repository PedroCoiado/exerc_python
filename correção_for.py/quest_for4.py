numeros = []
for x in range(0,5):
    s = int(input("Informe um valor"))
    numeros.append(s)

m = numeros[0]
for x in numeros:
    if x > m:
        m = x
print("O maior valor é "+str(m))