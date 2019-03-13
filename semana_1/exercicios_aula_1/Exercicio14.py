lista = [1,2,3,4]

resultado = []

for index, numero in enumerate(lista):
    resultado.append(sum(lista[:index+1]))

print(resultado)