#Exercicio 07
#Faça um programa que receba uma string e responda se ela tem algua vogal,
#Se sim, quais são? E tambem diga se ela e uma frase ou nao?

string = input('Digite algo: ')
vogais = []
vogal = 'aeiou'

for letra in string:
    if letra in vogal:
        vogais = vogais.append(letra)

if string.count(' '):
    print('É frase!')

if len(vogais) > 0:
    print('As vogais encontradas foram: {}'.format(set(vogais)))