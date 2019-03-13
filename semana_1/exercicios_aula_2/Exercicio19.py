'''
lista = ['keep','remove','keep','remove','keep','remove']
n_lista = []

for item in lista:
    if item == 'remove':
        n_lista = filter(lista.remove('remove'),lista)

print(list(n_lista))
'''

lista = ['keep','remove','keep','remove','keep','remove']
n_lista = []

