# Escreva um programa que receba o salário base de um funcionário, calcule e
# mostre seu salário a receber, sabendo-se que o funcionário tem gratificação de
# R$ 50 e paga imposto de 10% sobre o salário base.

sal_base = float(input("Informe o valor do salário base: "))
sal_receber = (sal_base + 50) * 0.90
print("O salário a receber é: ", sal_receber)