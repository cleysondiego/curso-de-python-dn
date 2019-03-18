'''
Dada uma função de soma:

'''

def soma (x, y):
    return x + y


'''
Faça assertivas de valores que você acredita serem coerentes com a função
'''

assert soma(1, 1) == 2
assert soma(-1, 2) == 1
assert soma('atapo','poata') == 'atapopoata', "Nao soma strings"
assert soma(1.2, 1.6) == 2.8
assert soma('ata', 4) == 'ata4'
assert soma(4, 'ata') == '4ata'
assert soma(1.3, 1) == 2.3