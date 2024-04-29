# Escreva um programa que receba dois números maiores que zero, calcule e
# mostre um elevado ao outro.

import math

while True:
    num1 = int(input("Informe a base: "))
    if num1 <=0:
        print("Número inválido. O programa será encerrado.")
        break

    num2 = int(input("Informe o expoente: "))
    if num2 <= 0:
        print("Número inválido. O programa será encerrado.")
        break
    print(f"{num1} elevado a {num2} = {math.pow(num1, num2)}")
    break
