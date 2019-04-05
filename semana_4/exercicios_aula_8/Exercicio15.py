class BichinhoVirtualPlusPlus:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f'''Nome: {self.nome}
Fome: {self.fome}
Saude: {self.saude}
Idade: {self.idade}'''

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def fomeBicho(self, comida):
        if self.fome < 100 and self.fome >= 0:
            self.fome += comida

    def saudeBicho(self):
        if self.saude < 100 and self.fome >= 0:
            self.saude += 1

    def idadeBicho(self):
        if self.idade < 70 and self.idade >= 0:
            self.idade += 1

    def humorBicho(self, tempoBrincando):
        return (self.fome + self.saude + self.idade + tempoBrincando) / 4

if __name__ == '__main__':
    meubicho = BichinhoVirtualPlusPlus('Lili', 16, 50, 30)
    print(meubicho.humorBicho(30))
    meubicho.fomeBicho(3)
    meubicho.fomeBicho(20)
    print(meubicho.humorBicho(40))
    print(meubicho)
