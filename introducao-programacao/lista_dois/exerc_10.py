# A Escreva um programa que receba dois números e execute uma das
# operações listadas a seguir, de acordo com a escolha do usuário. Se for
# digitada uma opção inválida, mostre mensagem de erro e termine a
# execução do programa. As opções são: a) O primeiro número elevado ao
# segundo número. b) Raiz quadrada de cada um dos números. c) Raiz cúbica
# de cada um dos números.

import math as m

num1 = int(input("Entre com o primeiro número: "))
num2 = int(input("Entre com o segundo número: "))
opcao = int(input("1 - Número um elevado ao segundo número\n2 - Raiz quadrada de cada um dos números\n3 - Raiz cúbica de cada um dos números"))

if opcao != 1 and opcao != 2 and opcao != 3:
    print("A opção informada não é válida, o programa será encerrado.")
elif opcao == 1:
    elevado = m.pow(num1, num2)
    print(f"{num1} elevado a {num2}: {elevado}")
elif opcao == 2:
    raiz_um = m.sqrt(num1)
    raiz_dois = m.sqrt(num2)
    print(f"Raiz quadrada de {num1} = {raiz_um}\nRaiz quadrada de {num2} = {raiz_dois}")
else:
    raiz_um = num1 ** (1/3)
    raiz_dois = num2 ** (1/3)
    print(f"Raiz cúbida de {num1} = {raiz_um}\nRaiz cúbica de {num2} = {raiz_dois}")