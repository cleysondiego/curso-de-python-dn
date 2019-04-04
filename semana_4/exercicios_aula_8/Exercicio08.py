class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self, comida):
        self.bucho.append(comida)
        self.verBucho()

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop()

    def __repr__(self):
        return f'Macaco: {self.nome}'


if __name__ == '__main__':
    macaco1 = Macaco('Orangotango', ['Banana', 'Peixe', 'Folha'])
    macaco2 = Macaco('Mandril', ['Gafanhoto', 'Arroz', 'Ovos'])
    macaco1.verBucho()
    macaco2.verBucho()
    macaco1.digerir()
    macaco2.digerir()
    macaco1.verBucho()
    macaco2.verBucho()
    macaco1.comer(macaco2)
    macaco2.comer(macaco1)
