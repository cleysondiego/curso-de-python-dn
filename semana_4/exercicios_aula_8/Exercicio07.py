class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def fomeBicho(self):
        ...

    def saudeBicho(self):
        ...

    def idadeBicho(self):
        ...

    def humorBicho(self):
        ...

if __name__ == '__main__':
    meubicho = BichinhoVirtual('Lili', 'Ok', 'Mal', 30)
