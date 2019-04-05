class ContaDeInvestimentos:
    def __init__(self, numero_da_conta: int, nome: str, taxaJuros: float, saldo = 0):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionarJuros(self):
        self.saldo = (self.saldo * (self.taxaJuros/100)) + self.saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor_deposito):
        self.saldo += valor_deposito

    def saque(self, valor_sacar):
        if self.saldo > valor_sacar:
            self.saldo -= valor_sacar
            print(f'Sacando o valor de: {valor_sacar}')
        else:
            print('Você não possui saldo suficiente')

if __name__ == '__main__':
    conta_cleyson = ContaDeInvestimentos(1321, 'Cleyson', 10, 1000)
    print(conta_cleyson.saldo)
    conta_cleyson.adicionarJuros()
    print(conta_cleyson.saldo)
