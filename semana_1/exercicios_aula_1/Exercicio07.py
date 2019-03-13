#Exercicio 07
#Faça um programa que receba uma string e responda se ela tem algua vogal,
#Se sim, quais são? E tambem diga se ela e uma frase ou nao?

string = input('Digite algo: ')

if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
    print('O que você digitou, tem vogais.')

    if 'a' in string:
        print('Contem a letra A')
    
    if 'e' in string:
        print('Contem a letra E')
    
    if 'o' in string:
        print('Contem a letra O')
    
    if 'i' in string:
        print('Contem a letra I')
    
    if 'u' in string:
        print('Contem a letra U')
    
if ' ' in string:
    print('Você digitou uma frase')