# Escreva um programa que receba dois números e mostre o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if (num1 > num2):
    menor = num2
else:
    maior = num1

print("O menor número é ", menor)