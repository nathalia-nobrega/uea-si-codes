# Escreva um programa que receba as três notas de um aluno e uma letra. Se
# a letra for A, o programa deve imprimir a média Aritmética das notas do
# aluno. Se a letra for P, o programa deve imprimir a média ponderada das
# avaliações, assumindo os pesos 5, 3 e 2.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
opcao = input('Digite "A" para a média aritmética e P para a ponderada: ')

if opcao != 'A' or opcao != 'P':
    print("Opção inválida, o programa será encerrado!")
elif opcao == 'A':
    media = (nota1 + nota2 + nota3) / 3
    print("Sua média aritmética foi: {}".format(media))
elif opcao == 'P':
    media = ((nota1 * 5) + (nota2 * 2) + (nota3 * 3)) / 5 + 2 + 3
    print("Sua média ponderada foi: {}".format(media))
