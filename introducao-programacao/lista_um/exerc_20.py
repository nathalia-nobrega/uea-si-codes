# Escreva um programa que receba o custo de um espetáculo teatral e o preço
# do convite desse espetáculo. Esse programa deverá calcular e mostrar a
# quantidade de convites que devem ser vendidos para que, pelo menos, o
# custo do espetáculo seja alcançado.

import math

custo_show = float(input("Custo do espetáculo: "))
preco_show = float(input("Preço do convite: "))

qtd_convites = math.ceil(custo_show/preco_show)

print("A quantidade de convites que devem ser vendidos é: ", qtd_convites)
