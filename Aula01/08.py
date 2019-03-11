#Exercicio 08
#Faça um programa que receba uma data de nascimento (15/07/87) e imprima
#"Voce nasceu em <Dia> de <mes> de <ano>"

nascimento = input('Digite sua data de nascimento: ')

ano, mes, dia = list(nascimento.split('/'))

print('Voce nasceu em {0} de {1} de {2}'.format(ano,mes,dia))