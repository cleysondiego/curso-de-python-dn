'''
Dada uma lista:

[‘keep’, ‘remove’, ‘keep’, ‘remove’, ‘keep’, ‘remove’]
Usando a função map transforme o primeiro carácter em maiúsculo.

'''

lista = ['keep','remove','keep','remove','keep','remove']

n_lista = map(lambda x: x.capitalize(), lista)

print(list(n_lista))
