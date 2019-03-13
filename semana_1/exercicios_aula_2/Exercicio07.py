Entrada = [1,2,3]
Entrada = Entrada[::-1]

print(Entrada)

for item in Entrada[::-1]:
    Entrada.insert(item,item)

print(Entrada)