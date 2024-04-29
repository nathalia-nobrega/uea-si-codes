# Escreva um programa que receba a quantidade de dinheiro em reais que
# uma pessoa que vai viajar possui. Ela vai passar por vários países e precisa
# converter seu dinheiro em dólares, marco alemão e libra esterlina. Sabe- -se
# que a cotação do dólar é de R$ 1,80; do marco alemão, de R$ 2,00; e da libra
# esterlina, de R$ 3,57. O programa deve fazer as conversões e mostrá-las.

qtd_reais = float(input("Informe o valor disponível em reais: "))

reais_dolares = round(qtd_reais/1.80, 2)
reais_marco = qtd_reais/2.0
reais_libras = round(qtd_reais/3.57, 2)

print(f"\nReais -> Dólares: {reais_dolares}\n Reais -> Marco Alemão: {reais_marco}\nReais -> Libras esterlinas: {reais_libras}")
