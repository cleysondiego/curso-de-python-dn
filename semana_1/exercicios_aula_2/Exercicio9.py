saudacao = input('Digite uma saudação: ')
nome = input('Digite um nome: ')

def saudacao_user(saudacao, nome):
    return f'{saudacao} {nome}'

print(saudacao_user(saudacao, nome))