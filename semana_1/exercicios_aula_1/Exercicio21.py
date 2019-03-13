lista = []
dicionario = {}

condicao = 's'

def cubo(lista):
    for x in lista:
        return x**3

def quadrado(lista):
    for x in lista:
        return x**2

while condicao == 's':
    lista.append(int(input('Digite um valor: ')))
    condicao = input('Deseja inserir outro valor? (s/n) ')

dicionario['lista'] = lista
dicionario['lista ao quadrado'] = quadrado(lista)
dicionario['lista ao cubo'] = cubo(lista)
print(dicionario)
#gitlab.com/dunossauro/curso-de-python
