class Retangulo:
    def __init__(self, LadoA: float, LadoB: float):
        self.LadoA = LadoA
        self.LadoB = LadoB

    def alterar_valor_dos_lados(self, novo_LadoA, novo_LadoB):
        self.LadoA = novo_LadoA
        self.LadoB = novo_LadoB

    def valor_dos_lados(self):
        return self.LadoA, self.LadoB

    def calcular_area(self):
        return self.LadoA * self.LadoB

    def calcular_perimetro(self):
        return 2 * (self.LadoA + self.LadoB)
