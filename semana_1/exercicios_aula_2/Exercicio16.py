#GoF < Funções
'''
Faça uma função que receba uma função e um número. Ela deve retornar uma lista com todos os números em ordem crescente até aquele valor:

aplica_em_lote(soma_1, 3) -> [1, 2, 3, 4]
DICA:
    O index inicia em 0
'''
def soma_1(valor):
    return valor+1

def aplica_em_lote(funcao, numero):
    lista = []
    for n in range(numero):
        lista.append(funcao(n))
    return lista

print(aplica_em_lote(soma_1, 5))
