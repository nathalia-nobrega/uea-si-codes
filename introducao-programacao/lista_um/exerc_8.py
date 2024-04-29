# Escreva um programa que receba o valor de um depósito e o valor da taxa de
# juros, calcule e mostre o valor do rendimento e o valor total depois do
# rendimento.

val_deposito =  float(input("Informe o valor do depósito: "))
taxa_juros = int(input("Informe a taxa de juros (%): "))
val_juros = taxa_juros/100
val_rendimento = val_deposito * val_juros
val_total = val_deposito + val_rendimento
print(f"Valor do rendimento: {val_rendimento} --- Valor total: {val_total}.")



