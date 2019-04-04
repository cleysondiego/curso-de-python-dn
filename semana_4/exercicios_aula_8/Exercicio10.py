class BombaCombustivel:
    def __init__(self):
        self.tipoCombustivel = ['Gasolina Adtivada', 'Gasolina Comum', 'Alcool']
        self.valorLitro = {'Gasolina Adtivada': 4.5, 'Gasolina Comum': 3.5, 'Alcool': 2.60}
        self.quantidadeCombustivel = {'Gasolina Adtivada': 300, 'Gasolina Comum': 600, 'Alcool': 700}

    def abastecerPorValor(self, valor, tipoCombustivel):
        for key, value in self.valorLitro.items():
            if key == tipoCombustivel:
                qntdLitros = valor/self.valorLitro[key]
                self.alterarQuantidadeCombustivel(tipoCombustivel, qntdLitros)
                return f'Abasteceu com {qntdLitros} litros'

    def abastecerPorLitros(self, litrosAbastecidos, tipoCombustivel):
        for key, value in self.valorLitro.items():
            if key == tipoCombustivel:
                self.alterarQuantidadeCombustivel(tipoCombustivel, litrosAbastecidos)
                return f'O consumidor deverá pagar: R${(litrosAbastecidos*value)}'

    def alterarValor(self, combustivel, novoValor):
        self.valorLitro[combustivel] = novoValor

    def alterarCombustivel(self, combustivel, novoCombustivel):
        self.tipoCombustivel.remove(combustivel)
        self.tipoCombustivel.append(novoCombustivel)

    def alterarQuantidadeCombustivel(self, combustivel, litrosAbastecidos):
        self.quantidadeCombustivel[combustivel] -= litrosAbastecidos
        # altera a quantidade de combustivel restante na bomba.
        # sempre que acontecer o abastecer por valor ou por litro,
        # reduz a quantidade total na bomba.

if __name__ == '__main__':
    bomba01 = BombaCombustivel()
    print(bomba01.abastecerPorValor(150, 'Gasolina Adtivada'))
    print(bomba01.abastecerPorLitros(40, 'Alcool'))
    print(bomba01.quantidadeCombustivel)
