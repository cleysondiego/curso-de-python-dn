class Bola:
    def __init__(self, cor: str, circunferencia: str, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor: str):
        self.cor = nova_cor

    def mostra_cor(self):
        return self.cor


bolinha = Bola('Verde', 'Grande', 'Couro')
print(bolinha.mostra_cor())
bolinha.troca_cor('Amarelo')
print(bolinha.mostra_cor())
