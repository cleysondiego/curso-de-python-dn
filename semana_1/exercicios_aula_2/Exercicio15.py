def soma2(num):
    return num+2

def sub2(num):
    return num-2

def reaplica(funcao, num):
    return funcao(funcao(num))

print(reaplica(soma2, 2))
print(reaplica(sub2, 2))
