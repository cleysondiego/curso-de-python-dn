def calcula_mediana(lista):
    listaA = sorted(lista)
    tamanho = len(lista)
    meio = tamanho//2

    if tamanho % 2:
        return listaA[meio]
    else:
        menor = meio-1
        maior = meio
        return(listaA[menor] + listaA[maior])/2

print(calcula_mediana([1,2,3]))