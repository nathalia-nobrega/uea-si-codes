# Escreva um programa que receba o salário base de um funcionário, calcule e
# mostre o salário a receber, sabendo-se que o funcionário tem gratificação de
# 5% sobre o salário base e paga imposto de 7% também sobre o salário base.

sal_base = float(input("Qual o salário base do funcionário? "))
sal_receber = sal_base * 1.05 * 0.93
print("O salário a receber, sabendo que há '5%' de gratificação e 7'%' de imposto é: ", sal_receber)