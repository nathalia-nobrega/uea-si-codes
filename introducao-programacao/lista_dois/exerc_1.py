# Escreva um programa que receba quatro notas de um aluno, calcule e
# mostre a média aritmética das notas e a mensagem de aprovado ou
# reprovado, considerando para aprovação média 6,0.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if (media < 6):
    print("\nREPROVADO COM MÉDIA ", media)
else:
    print("\nAPROVADO COM MÉDIA ", media)
