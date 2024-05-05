# Escreva um programa que receba três valores (A, B e C) e verifique se
# podem formar os lados de um triângulo. Caso positivo, imprima se o
# triângulo é equilátero, isósceles ou escaleno. Do contrário, imprima “NÃO é
# triangulo”

# Condição de existência de triângulos: um lado deve ser menor que a soma dos outros dois lados

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if (num1 > num2 + num3 or num2 > num1 + num3 or num3 > num1 + num2):
    print("Não é possível formar um triângulo")
elif (num1 == num2 == num3):
    print("O triângulo é equilátero")
elif((num1 == num2 and num1 != num3) or (num2 == num3 and num2 != num1)):
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
