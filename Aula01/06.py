#Exercicio 06
#Faça um programa que pergunte o preço de tres produtos e informe qual o produto voce deve comprar
#Sabendo que a decisao e sempre pelo mais barato

produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))
produto3 = float(input('Digite o preço do produto 3: '))

menorValor = min(produto1, produto2, produto3)

print(f"Menor valor: {menorValor}")