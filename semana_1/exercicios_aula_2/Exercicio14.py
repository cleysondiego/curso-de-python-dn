numero = int(input('Digite um número: '))

def romeujulieta(numero):
    return 'Romeu e Julieta' if ((numero % 3) == 0 and (numero % 5) == 0) else numero

print(romeujulieta(numero))