# Sabe-se que:
# • pé = 12 polegadas
# • 1 jarda = 3 pés
# • 1 milha = 1,760 jarda
# Escreva um programa que receba uma medida em pés, faça as
# conversões a seguir e mostre os resultados.
# a) polegadas;
# b) jardas;
# c) milhas.

medida_pes = int(input("Informe uma medida em pés: "))
pes_para_polegadas = medida_pes * 12
pes_para_jardas = medida_pes/3
pes_para_milhas = pes_para_jardas/1.760

print(f"Pés -> Polegadas: {pes_para_polegadas}")
print(f"Pés -> Jardas: {pes_para_jardas}")
print(f"Pés -> Milhas: {pes_para_milhas}")