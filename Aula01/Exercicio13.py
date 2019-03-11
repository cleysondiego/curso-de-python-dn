lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input('Digite um número inteiro: '))

for num in lista:
    print('{} x {} = {}'.format(numero, num, (numero*num)))
