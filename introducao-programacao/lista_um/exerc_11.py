# Escreva um programa que receba um número positivo e maior que zero,
# calcule e mostre:
# a. O número digitado ao quadrado;
# b. O número digitado ao cubo;
# c. A raiz quadrada do número digitado;

import math

num = int(input("Entre com um número positivo e maior que zero: "))

while True:
    if num <= 0:
        print("O número informado não é válido. O programa será encerrado.")
        break
    print(f"{num}² = {num*num}\n{num}³ = {math.pow(num,3)}\nraiz de {num} = {math.sqrt(num)}")
    break
