lista = ['keep','remove','keep','remove','keep','remove']
n_lista = []

def remover(lista):
	remover = ['remove']
	
	return False if lista in remover else True

n_lista = filter(remover, lista)
print(list(n_lista))
