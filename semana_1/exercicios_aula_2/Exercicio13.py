numero = int(input('Digite um número: '))

def goiabada(numero):
    return 'goiabada' if ((numero % 5) == 0) else numero

print(goiabada(numero))