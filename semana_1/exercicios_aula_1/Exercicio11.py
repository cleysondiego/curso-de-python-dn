string = input('Digite algo: ')
nome = input('Digite seu nome: ')

for letra in string:
    if letra in 'aeiou':
        print(nome)
    else:
        print(letra)