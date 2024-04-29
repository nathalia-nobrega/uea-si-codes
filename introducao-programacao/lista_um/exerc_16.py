# Escreva um programa que receba o número de horas trabalhadas e o valor
# do salário mínimo, calcule e mostre o salário a receber, seguindo estas
# regras:
# a. A hora trabalhada vale a metade do salário mínimo.
# b. O salário bruto equivale ao número de horas trabalhadas
# multiplicado pelo valor da hora trabalhada.
# c. O imposto equivale a 3% do salário bruto.
# d. O salário a receber equivale ao salário bruto menos o imposto.

horas_trabalhadas = int(input("Informe o número de horas trabalhadas: "))
sal_minimo = float(input("Informe o salário mínimo: "))

hora = sal_minimo/2
sal_bruto = horas_trabalhadas * hora
imposto = sal_bruto * 0.03
sal_receber = sal_bruto - imposto

print("O salário a receber é R$", sal_receber)