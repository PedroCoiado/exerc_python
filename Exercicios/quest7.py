# As Organizações Tabajara resolveram dar um aumento de salário aos seus 
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes
# Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério, baseado no salário atual:



salario = float(input('Salário do empregado: '))

if (salario <= 280):
        percentual = 20
elif (salario <= 700):
        percentual = 15
elif (salario <= 1500):
        percentual = 10
else:
        percentual = 5

print('Salario atual: R$ ', salario)
print('Percentual: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento
    
print('Aumento: R$ ',aumento)
print('Novo salário: R$ ', novo_salario)
