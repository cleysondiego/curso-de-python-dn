class ContaDeInvestimentos:
    def __init__(self, numero_da_conta: int, nome: str, saldo = 0, taxaJuros: float):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionarJuros(self):
        self.taxaJuros = 10

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
    conta_cleyson = ContaCorrente(1321, 'Cleyson')
    print(conta_cleyson.saldo)
    conta_cleyson.deposito(300)
    print(conta_cleyson.saldo)
    conta_cleyson.saque(150)
    print(conta_cleyson.saldo)
