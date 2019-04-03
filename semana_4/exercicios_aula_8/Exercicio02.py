class Quadrado:
    def __init__(self, tamanho_do_lado: float):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_do_lado(self, novo_tamanho: float):
        self.tamanho_do_lado = novo_tamanho

    def retornar_valor_do_lado(self):
        return self.tamanho_do_lado

    def calcular_area(self):
        return self.tamanho_do_lado*4


quadradito = Quadrado(12.5)
print(quadradito.retornar_valor_do_lado())
quadradito.mudar_valor_do_lado(5.5)
print(quadradito.retornar_valor_do_lado())
print(quadradito.calcular_area())
