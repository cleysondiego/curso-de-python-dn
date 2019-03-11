lista = input('Digite números e os separe com vírgula: ')
lista.split(',')

for item in lista:
    print(lista[item] + item)
