class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # def mostrarValoresPonto(self):
        # pontox=Ponto().x
        # pontoy=Ponto().y
        # return f'{pontox}, {pontoy}'

    def centroRetangulo(self):
        return Ponto((self.largura/2), (self.altura/2))


if __name__ == '__main__':
    retangulo1 = Retangulo(3, 4)
    retangulo2 = Retangulo(5, 6)
    retangulo3 = Retangulo(15, 50)
