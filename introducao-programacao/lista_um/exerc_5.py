# Escreva um programa que receba o salário de um funcionário e o percentual
# de aumento, calcule e mostre o valor do aumento e o novo salário.

salario = float(input("Qual o salário do funcionário? "))
percentual = int(input("Qual o percentual de aumento? "))

novo_salario = salario + salario * (percentual/100)
valor_aumento = novo_salario - salario

print("\n")
print(f"Valor do aumento: {valor_aumento}")
print(f"Novo salário: {novo_salario}")
