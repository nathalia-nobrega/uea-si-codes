# O custo ao consumidor de um carro novo é a soma do preço de fábrica com
# o percentual de lucro do distribuidor e dos impostos aplicados ao preço de
# fábrica. Escreva um programa que receba o preço de fábrica de um veículo,
# o percentual de lucro do distribuidor e o percentual de impostos, calcule e
# mostre:
# a. O valor correspondente ao lucro do distribuidor;
# b. O valor correspondente aos impostos;
# c. O preço final do veículo.

prec_fabrica = float(input("Preço de fábrica do veículo: "))
perc_distribuidor = int(input("Percentual de lucro do distribuidor: "))
perc_impostos = int(input("Percentual de impostos: "))

val_distribuidor = prec_fabrica * (perc_distribuidor / 100)
val_impostos = prec_fabrica * (perc_impostos / 100)
prec_final = prec_fabrica + val_distribuidor + val_impostos

print("O preço final do veículo ao consumidor é R$",prec_final)
