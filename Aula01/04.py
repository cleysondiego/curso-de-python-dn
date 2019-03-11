#Exercicio 04
#Faça um programa que pela 2 números inteiros e um número real. Calcule e mostre:

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
numero3 = float(input('Digite um número real: '))

resultado01 = (numero1*2)*(numero2/2)
print(f'O produto do dobro do primeiro com metade do segundo é: {resultado01}')

resultado02 = (numero1*3)+numero3
print(f'A soma do triplo  do primeiro com o terceiro é: {resultado02}')

resultado03 = (numero3**3)
print(f'O terceiro elevado ao cubo: {resultado03}')
