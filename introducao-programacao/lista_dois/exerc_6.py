# Escreva um programa que peça do usuário a altura de cinco mulheres e
# imprima:
# a. número de mulheres com altura ABAIXO da média;
# b. número de mulheres com altura ACIMA da média;
# c. número de mulheres com estatura mediana;

alt1 = float(input('Entre com a primeira altura: '))
alt2 = float(input('Entre com a segunda altura: '))
alt3 = float(input('Entre com a terceira altura: '))
alt4 = float(input('Entre com a quarta altura:'))
alt5 = float(input('Entre com a quinta altura: '))

media = (alt1 + alt2 + alt3 + alt4 + alt5) / 5
print("\nA média de altura é: ", media)

# a. número de mulheres com altura ABAIXO da média;
numAbaixo = 0
if (alt1 < media): numAbaixo += 1
if (alt2 < media): numAbaixo += 1
if (alt3 < media): numAbaixo += 1
if (alt4 < media): numAbaixo += 1
if (alt5 < media): numAbaixo += 1

# b. número de mulheres com altura ACIMA da média;
numAcima = 0
if (alt1 > media): numAcima += 1
if (alt2 > media): numAcima += 1
if (alt3 > media): numAcima += 1
if (alt4 > media): numAcima += 1
if (alt5 > media): numAcima += 1

# c. número de mulheres com estatura mediana;
numMedia = 0
if (alt1 == media): numMedia += 1
if (alt2 == media): numMedia += 1
if (alt3 == media): numMedia += 1
if (alt4 == media): numMedia += 1
if (alt5 == media): numMedia += 1

print("\nNúmero de mulheres abaixo da média: ", numAbaixo)
print("\nNúmero de mulheres acima da média: ", numAcima)
print("\nNúmero de mulheres com estatura mediana: ", numMedia)
