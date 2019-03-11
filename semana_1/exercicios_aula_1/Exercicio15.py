digitUser = input('Digite números e os separe com vírgula: ')

lista = digitUser.split(',')
for a in lista:
    for b in lista:
        print([a, b])
