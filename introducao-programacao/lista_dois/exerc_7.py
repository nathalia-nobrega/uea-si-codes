# Escreva um programa que leia os dados de 5 alunos, contendo a altura e o
# código do sexo de cada um (onde 1 == masculino e 2 == feminino), calcule e
# imprima:
# a. A maior e a menor altura da turma
# b. A média de altura da turma;
# c. A média de altura das mulheres;
# d. A menor altura das mulheres;
# e. A média de altura dos homens;
# f. A maior altura dos homens;

alt1 = float(input('Entre com a primeira altura: '))
sexo1 = int(input('Entre com o sexo do primeiro aluno (1 = homem ou 2 = mulher): '))

alt2 = float(input('Entre com a segunda altura: '))
sexo2 = int(input('Entre com o sexo do segundo aluno (1 = homem ou 2 = mulher): '))

alt3 = float(input('Entre com a terceira altura: '))
sexo3 = int(input('Entre com o sexo do terceiro aluno (1 = homem ou 2 = mulher): '))

alt4 = float(input('Entre com a quarta altura:'))
sexo4 = int(input('Entre com o sexo do quarto aluno (1 = homem ou 2 = mulher): '))

alt5 = float(input('Entre com a quinta altura: '))
sexo5 = int(input('Entre com o sexo do quinto aluno (1 = homem ou 2 = mulher): '))

# a. A maior e a menor altura da turma
maior = max(alt1, alt2, alt3, alt4, alt5)
menor = min(alt1, alt2, alt3, alt4, alt5)
print(f"A maior altura da turma: {maior}\nA menor altura da turma: {menor}")

# b. A média de altura da turma;
media = (alt1 + alt2 + alt3 + alt4 + alt5) / 5
print(f"A média de altura da turma é {media:.2f}")

# c. A média de altura das mulheres;
somaMulher = 0
qtdMulher = 0

if (sexo1 == 2):
    qtdMulher += 1
    somaMulher += alt1
if (sexo2 == 2):
    qtdMulher += 1
    somaMulher += alt2
if (sexo3 == 2):
    qtdMulher += 1
    somaMulher += alt3
if (sexo4 == 2):
    qtdMulher += 1
    somaMulher += alt4
if (sexo5 == 2):
    qtdMulher += 1
    somaMulher += alt5

mediaMulher = somaMulher/qtdMulher
print(f"A média de altura das mulheres é: {mediaMulher}")

# d. A menor altura das mulheres;

alturasMulheres = []

if (sexo1 == 2):
    alturasMulheres.append(alt1)

if (sexo2 == 2):
    alturasMulheres.append(alt2)

if (sexo3 == 2):
    alturasMulheres.append(alt3)

if (sexo4 == 2):
    alturasMulheres.append(alt4)

if (sexo5 == 2):
    alturasMulheres.append(alt5)

print(f"A menor altura das mulheres é: {min(alturasMulheres)}")

# e. A média de altura dos homens;
somaHomem = 0
qtdHomem = 0

if (sexo1 == 1):
    qtdHomem += 1
    somaHomem += alt1
if (sexo2 == 1):
    qtdHomem += 1
    somaHomem += alt2
if (sexo3 == 1):
    qtdHomem += 1
    somaHomem += alt3
if (sexo4 == 1):
    qtdHomem += 1
    somaHomem += alt4
if (sexo5 == 1):
    qtdHomem += 1
    somaHomem += alt5

mediaHomem = somaHomem/qtdHomem
print(f"A média de altura dos homens é {mediaHomem}")

# f. A maior altura dos homens;
alturasHomens = []

if (sexo1 == 2):
    alturasHomens.append(alt1)

if (sexo2 == 2):
    alturasHomens.append(alt2)

if (sexo3 == 2):
    alturasHomens.append(alt3)

if (sexo4 == 2):
    alturasHomens.append(alt4)

if (sexo5 == 2):
    alturasHomens.append(alt5)

print(f"A menor altura dos homens é: {min(alturasHomens)}")
