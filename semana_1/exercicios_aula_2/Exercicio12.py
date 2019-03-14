numero = int(input('Digite um número: '))

'''
def queijo(numero):
    if ((numero % 3) == 0):
        return 'queijo'
    else:
        return numero
'''

def queijo2(numero):
    return 'queijo' if ((numero % 3) == 0) else numero

print(queijo2(numero))
