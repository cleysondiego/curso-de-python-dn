class Fila:
    def __init__(self):
        self.fila = []

    def entrar(self, pessoa):
        self.fila.append(pessoa)

    def sair(self):
        self.fila.pop(0)

    def __repr__(self):
        return str(self.fila)


fila = Fila()

fila.entrar('Cleyson')
fila.entrar('Aadaadf')
print(fila)

fila.sair()
print(fila)