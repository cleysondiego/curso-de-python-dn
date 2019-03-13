lista = ['keep','remove','keep','remove','keep','remove']

n_lista = filter(lista.remove('remove'),lista)

print(list(n_lista))