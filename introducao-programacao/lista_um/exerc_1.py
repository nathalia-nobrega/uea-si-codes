# Escreva um programa que receba quatro números inteiros, calcule e mostre a
# soma desses números. 

sum = 0
cont = 0
while cont < 4:
    numero = int(input("Digite um número: "))
    sum += numero
    cont+=1
print(f"A soma dos números digitados foi: {sum}")
