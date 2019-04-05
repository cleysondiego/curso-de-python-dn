class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.ponto = Ponto(0, 0)
        self.menu()

    def imprimirValores(self):
        print(f'X: {self.ponto.x}\nY: {self.ponto.y}')

    def centroRetangulo(self):
        self.ponto.x, self.ponto.y = (self.largura/2), (self.altura/2)
        self.imprimirValores()

    def alterarValores(self, larg, alt):
        self.largura = larg
        self.altura = alt

    def menu(self):
        while True:
            escolha = int(input('Deseja alterar os valores da largura e altura?\n1 - Sim\n2 - Não\nEscolha: '))
            if escolha == 1:
                escolha_largura = float(input('Digite o novo valor da largura: '))
                escolha_altura = float(input('Digite o novo valor da altura: '))
                self.alterarValores(escolha_largura, escolha_altura)
            else:
                print('Saindo...')
                break



if __name__ == '__main__':
    retangulo1 = Retangulo(3, 4)
    retangulo1.imprimirValores()
    retangulo1.centroRetangulo()
    retangulo2 = Retangulo(5, 6)
    retangulo3 = Retangulo(15, 50)
