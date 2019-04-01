arquivo = open('exercicio05.txt', 'w')


def tab1(x):
    return f'{x} x 10 = {x*10}\n'


for item in range(1, 11):
    arquivo.writelines(tab1(item))

