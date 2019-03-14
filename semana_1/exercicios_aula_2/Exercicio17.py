'''
Faça uma função que receba uma função e uma lista de números, 
aplique essa função a todos os valores da lista e retorne uma nova lista com os valores processados:

aplica(func, list) -> [func(list[0]), func(list[n]), ..]
aplica(soma_1, [1, 2, 3]) -> [2, 3, 4]
aplica(sub_1, [1, 2, 3]) -> [0, 1, 2]
'''

def soma_1(num):
    return num+1

def sub_1(num):
    return num-1

def aplicafuncao(func, lista):
    novalista = []
    for item in lista:
        novalista.append(func(item))
    
    return novalista

print(aplicafuncao(soma_1, [1, 2, 3]))
print(aplicafuncao(sub_1, [1, 2, 3]))
