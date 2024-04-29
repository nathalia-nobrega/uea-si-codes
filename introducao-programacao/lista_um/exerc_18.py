# Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos,
# para os quais fornece a quantidade de ração em gramas. A quantidade
# diária de ração fornecida para cada gato é sempre a mesma. Escreva um
# programa que receba o peso do saco de ração e a quantidade de ração
# fornecida para cada gato, calcule e mostre quanto restará de ração no saco
# após cinco dias.

peso_saco = int(input("Informe o peso do saco de ração (kg): "))
qtd_um = int(input("Informe a quantidade diária de ração para o primeiro gato (g): "))
qtd_dois = int(input("Informe a quantidade diária de ração para o segundo gato (g): "))

consumo_total = (qtd_um * 5) + (qtd_dois * 5)
resto = peso_saco - (consumo_total/1000)

print(f"\nApós 5 dias, o total consumido pelos gatos será de {consumo_total}g.\nA quantidade que restará no saco de ração será {resto}kg.")
