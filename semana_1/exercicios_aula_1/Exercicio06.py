#Exercicio 06
#Faça um programa que pergunte o preço de tres produtos e informe qual o produto voce deve comprar
#Sabendo que a decisao e sempre pelo mais barato

produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))
produto3 = float(input('Digite o preço do produto 3: '))

if produto1 < produto2 and produto3 and produto1:
    print('Compre o produto 1')
elif produto2 < produto1 and produto3:
    print('Compre o produto 2')
elif produto3 < produto1 and produto2:
    print('Compre o produto 3')
elif produto1 == produto2 and produto1 and produto2 < produto3:
    print('Compre o produto 1 ou 2')
elif produto1 == produto3 and produto1 and produto3 < produto2:
    print('Compre o produto 1 ou 3')
elif produto2 == produto3 and produto2 and produto3 < produto1:
    print('Compre o produto 2 ou 3')
else:
    print('Todos os preços são iguais!!')
