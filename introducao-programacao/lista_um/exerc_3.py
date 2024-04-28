# Escreva um programa que receba três notas e seus respectivos pesos, calcule e
# mostre a média ponderada.

nota1 = float(input("Entre com a nota um: "))
nota2 = float(input("Entre com a nota dois: "))
nota3 = float(input("Entre com a nota três: "))
print("\n")
peso1 = int(input("Entre com o peso um: "))
peso2 = int(input("Entre com o peso dois: "))
peso3 = int(input("Entre com o peso três: "))

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3))/(peso1 + peso2 + peso3)

print("A média ponderada foi: ", media)