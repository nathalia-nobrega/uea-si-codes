# Escreva um programa para calcular e mostrar o salário reajustado de um
# funcionário. O percentual de aumento encontra-se na tabela a seguir:
# <= 300.00 -->  35%
# > 300.00 --> 15%

salario = float(input("Entre com o salário do funcionário: "))

if salario <= 300.00:
    aumento = salario * 1.35
    print("O salário reajustado é: R$", aumento)
else:
    aumento = salario * 1.15
    print("O salário reajustado é: R$", aumento)