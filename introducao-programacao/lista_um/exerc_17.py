# Um trabalhador recebeu seu salário e o depositou em sua conta bancária.
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
# Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o
# saldo inicial da conta está zerado

salario = float(input("Informe o salário do trabalhador: "))
CPMF = 0.38 / 100
cheque_um = salario * CPMF
cheque_dois = salario * CPMF

saldo_final = salario - (cheque_um + cheque_dois)
print(f"Saldo final da conta após dois cheques de ({cheque_um}): {saldo_final}")
