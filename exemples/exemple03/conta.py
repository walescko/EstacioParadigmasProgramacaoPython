class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        n = len(clientes)

    def clientesConta(self):
        for i in self.clientes:
            print(f'Nome: {i.nome}, CPF: {i.nome}, Endereço: {i.endereco}')
    def infoConta(self):
        print(f'INFORMAÇÕES DA CONTA')
        self.clientesConta()
        print(f"Número da conta: {self.numero}")
        print(f"Saldo da Conta: R$ {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transferirValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Saldo insufiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
        return "Transferência Realizada"

    def gerarSaldo(self):
        print('Saldo da Conta')
        self.clientesConta()
        print(f'Numero: {self.numero} \nsaldo: R$ {self.saldo}')
