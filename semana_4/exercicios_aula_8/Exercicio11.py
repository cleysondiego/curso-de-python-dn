class Carro:
    def __init__(self, consumo):
        self.combustivel = 0
        self.consumo = consumo

    def andar(self, distancia):
        if self.combustivel > 0:
            self.combustivel -= (distancia/self.consumo)
            return f'O carro andou {distancia} kms'

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros


if __name__ == '__main__':
    meuFusca = Carro(15)
    meuFusca.adicionarGasolina(20)
    meuFusca.andar(100)
    print(meuFusca.obterGasolina())
