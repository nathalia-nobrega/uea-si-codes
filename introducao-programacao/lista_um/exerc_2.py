# Escreva um programa que receba três notas, calcule e mostre a média
# aritmética.

cont = 0
sum = 0
while cont < 3:
    nota = int(input(f"Digite a nota {cont + 1}: "))
    sum += nota
    cont+=1

media = sum / 3

print(f"A média das notas digitadas foi: {media}")