'''
Usando as funções criadas nos exercícios 13, 14 e 15. Crie uma composição de funções que resolva os 3 casos:

EX:
f(x) -> Union[ID, goiabada, queijo, romeu e julieta]
f(3) -> ‘queijo’
f(5) -> ‘goiabada’
f(15) -> ‘romeu e julieta’
f(19) -> 19
'''

def Union(id):
    if ((id % 5) == 0) and ((id % 3) == 0):
        return 'Romeu e Julieta'
    elif (id % 5) == 0:
        return 'Goiabada'
    elif (id % 3) == 0:
        return 'queijo'
    else:
        return id

id = int(input('Digite um número: '))

print(Union(id))