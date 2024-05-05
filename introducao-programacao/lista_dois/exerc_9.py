# Escreva um programa que receba dois números e execute as operações
# listadas a seguir, de acordo com a escolha do usuário. Se a opção digitada for inválida, mostre uma mensagem de erro e termine a
# execução do programa. Lembre-se de que, na operação 4, o segundo número deve ser diferente de zero.

num1 = int(input("Entre com o primeiro número: "))
num2 = int(input("Entre com o segundo número: "))
opcao = int(input("1 - Média entre os números digitados\n2 - Diferença do maior pelo menor\n3 - Produto entre os números digitados\n4 - Divisão do primeiro pelo segundo"))

if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
    print("A opção informada não é válida, o programa será encerrado.")
elif opcao == 1:
    print(f"Média entre os números: {(num1+num2)/2}")
elif opcao == 2:
    maior = max(num1, num2)
    menor = min(num1, num2)
    print(f"{maior} - {menor} : {(maior - menor)}")
elif opcao == 3:
    print(f"{num1} x {num2} = {(num1*num2)}")
else:
    if num2 == 0:
        num2 = int(input("O segundo número não deve ser zero. Digite um valor novo: "))
        print(f"{num1} / {num2} = {(num1/num2)}")
    else:
        print(f"{num1} / {num2} = {(num1/num2)}")