numero = int(input('Digit um numero: '))
string = input('Digite uma string: ')

def verifica(numero, string):
    if(len(string) == numero):
        return True
    else:
        return False

print(verifica(numero,string))
