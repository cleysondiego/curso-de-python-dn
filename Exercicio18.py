def quartil(lista, posicao):
    posicao_index = int(posicao * len(lista))
    return sorted(lista)[posicao_index]


print(quartil([1,2,3,4,5], 0.90))