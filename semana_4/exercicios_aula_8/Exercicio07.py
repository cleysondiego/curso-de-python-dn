class BichinhoVirtual:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def fomeBicho(self):
        if self.fome < 100 and self.fome >= 0:
            self.fome += 1

    def saudeBicho(self):
        if self.saude < 100 and self.fome >= 0:
            self.saude += 1

    def idadeBicho(self):
        if self.idade < 70 and self.idade >= 0:
            self.idade += 1

    def humorBicho(self):
        return (self.fome + self.saude + self.idade) / 3

if __name__ == '__main__':
    meubicho = BichinhoVirtual('Lili', 16, 50, 30)
    print(meubicho.humorBicho())
    meubicho.fomeBicho()
    meubicho.fomeBicho()
    print(meubicho.humorBicho())
