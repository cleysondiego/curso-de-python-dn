'''
Exercicio 03
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros custam R$80,00. Informe ao usuário a quantodades de latas de
tinta a serem compradas e o preço total.
'''

from math import ceil

tamanho = float(input('Digite o tamanho em metros quadrados: '))
litrosNecessarios = ceil(tamanho/3/18)

print("Quantidade {}, Preço: {}".format(litrosNecessarios,litrosNecessarios*80))
