'''
Dado o codigo:
faça assertivas em relacao ao que funciona e nao funciona nos seus casos de teste
'''

class Calc:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x + y

    def mult(self, x, y):
        return x + y

    def div(self, x, y):
        return x + y

#Testar com 0 é um teste ruim.
#Procurar PEP-008
assert Calc().add(0,0) == 0
assert Calc().sub(0,0) == 0
assert Calc().mult(0,0) == 0, "Função tá cagada tbm"
assert Calc().div(0,0) == 0, "Função cagadissima"