# Escreva um programa que receba duas notas, calcule e mostre a média
# aritmética e a mensagem que se encontra na tabela a seguir:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if (media < 3.0):
    print("REPROVADO COM MÉDIA ", media)
elif (media >= 3.0 and media < 7.0):
    print("EXAME FINAL COM MÉDIA ", media)
else:
    print("APROVADO COM MÉDIA ", media)

