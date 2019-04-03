from Exercicio03 import Retangulo

medida_LadoA = float(input('Digite o comprimento: '))
medida_LadoB = float(input('Digite a largura: '))
piso = float(input('Digite o m2 do piso: '))

sala = Retangulo(medida_LadoA, medida_LadoB)
area_da_sala = sala.calcular_area()
qnt_de_pisos = area_da_sala/piso

print(f'Será necessário {qnt_de_pisos} pisos.')
