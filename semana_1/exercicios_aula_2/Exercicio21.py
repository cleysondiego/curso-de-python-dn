'''
Dada uma lista:

[‘keep’, ‘remove’, ‘keep’, ‘remove’, ‘keep’, ‘remove’]
Usando a função reduce faça a somatória de todos os elementos da lista juntos
[‘a’, ‘abc’, ‘def’] -> 7

'''
from functools import reduce

#lista = ['keep','remove','keep','remove','keep','remove']
lista = ['a', 'abc', 'def']

resultado = len(reduce(lambda a, b: a + b, lista))

print(resultado)