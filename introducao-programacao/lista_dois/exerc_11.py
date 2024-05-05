# Uma empresa decide dar um aumento de 30% aos funcionários com
# salários inferiores a R$ 500,00. Escreva um programa que receba o salário
# do funcionário e mostre o valor do salário reajustado ou uma mensagem,
# caso ele não tenha direito ao aumento.

salario = float(input("Entre com o salário do funcionário: "))
if salario > 500.00:
    print("Este funcionário não tem direito ao aumento")
else:
    aumento = salario * 1.30
    print("O novo salário do funcionário é: R$", aumento)
