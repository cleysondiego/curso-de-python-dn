'''Exercicio 05
Faça um programa para a leitura de duas notas parciasi de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem aprovado se a media alcancada for maior ou igual a sete
reprovado se a media for menor do que sete
aprovado com distincao se a media for igual a dez
'''

Nota1 = int(input('Digite a primeira nota: '))
Nota2 = int(input('Digite a seguda nota: '))

media = (Nota1+Nota2)/2

if media >= 7 and  media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print("Aprovado com Distinção")
