# Escreva um programa que receba o ano de nascimento de uma pessoa e o
# ano atual, calcule e mostre:
# a. A idade dessa pessoa;
# b. Quantos anos ela terá em 2050.

import datetime

ano_atual = datetime.datetime.now().year

ano_nascimento = int(input("Qual seu ano de nascimento? "))
print(f"Idade ({ano_atual}): {ano_atual - ano_nascimento}\nIdade em 2050: {2050 - ano_nascimento}")
