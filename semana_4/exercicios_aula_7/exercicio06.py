arquivo = open('exercicio05.txt', 'r')

lista = []

for item in arquivo.readlines():
    lista.append(item.strip())


print(lista)