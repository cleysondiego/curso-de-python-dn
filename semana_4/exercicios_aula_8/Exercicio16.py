from Exercicio15 import BichinhoVirtualPlusPlus

class Fazenda:
    def __init__(self, nomebicho1, nomebicho2, nomebicho3):
        self.bichinho1=BichinhoVirtualPlusPlus(nomebicho1, 16, 50, 30)
        self.bichinho2=BichinhoVirtualPlusPlus(nomebicho2, 34, 62, 60)
        self.bichinho3=BichinhoVirtualPlusPlus(nomebicho3, 49, 100, 100)
        self.menu()

    def alimentarBichinhos(self):
        self.bichinho1.fomeBicho(4)
        self.bichinho2.fomeBicho(6)
        self.bichinho3.fomeBicho(1)

    def brincarBichinhos(self):
        self.bichinho1.humorBicho(30)
        self.bichinho2.humorBicho(2)
        self.bichinho3.humorBicho(5)

    def ouvirBichinhos(self):
        print(self.bichinho1)
        print(self.bichinho2)
        print(self.bichinho3)

    def menu(self):
        while True:
            escolha_jogador = int(input('1 - Alimentar todos os bichinhos\n2 - Brincar com todos os bichinhos\n3 - Ouvir a todos os bichinhos\nEscolha: '))
            if escolha_jogador == 1:
                self.alimentarBichinhos()
            elif escolha_jogador == 2:
                self.brincarBichinhos()
            elif escolha_jogador == 3:
                self.ouvirBichinhos()
            else:
                print('\nEscolha inválida, escolha uma das 3 opções válidas! \n')


if __name__ == '__main__':
    fazenda = Fazenda('Isma', 'el', 'vent')
