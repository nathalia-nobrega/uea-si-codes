# Sabe-se que o quilowatt de energia custa um quinto do salário mínimo.
# Escreva um programa que receba o valor do salário mínimo e a quantidade
# de quilowatts consumida por uma residência. Calcule e mostre:
# a. O valor de cada quilowatt;
# b. O valor a ser pago por essa residência;
# c. O valor a ser pago com desconto de 15%.

sal_minimo = float(input("Informe o salário mínimo: "))
qtd_kw_residencia = int(input("Informe a quantidade de quilowatts consumida por uma residência: "))

val_quilowatt = sal_minimo/5
val_pago_residencia = val_quilowatt * qtd_kw_residencia
val_pago_desconto = val_pago_residencia * 0.85

print(f"\na. O valor de cada quilowatt: {val_quilowatt}\nb. O valor a ser pago por essa residência: {val_pago_residencia}\nc. O valor a ser pago com desconto de 15%: {val_pago_desconto}")