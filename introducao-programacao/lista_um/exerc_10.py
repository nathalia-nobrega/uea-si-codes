# Escreva um programa que calcule e mostre a área de um círculo. Sabe-se que:
# Área = pi × R²

import math

raio = float(input("Informe o valor do raio do círculo: "))
area = round(math.pi * math.pow(raio, 2), 2)
print(f"A área do círculo de raio {raio} é {area}")
