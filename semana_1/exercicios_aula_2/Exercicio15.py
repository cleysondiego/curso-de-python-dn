def soma2(num):
    return num+2

def sub2(num):
    return num-2
    
def reaplica(soma2, num):
    return soma2(soma2(num))

print(reaplica(soma2, 2))
print(reaplica(sub2, 2))