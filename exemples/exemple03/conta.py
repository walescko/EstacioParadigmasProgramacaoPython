import datetime
from EstacioParadigmasProgramacaoPython.exemples.exemple03.extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataAbertura = datetime.datetime.today()
        self.extrato = Extrato()

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
        self.extrato.transacoes.append(['DEPOSITO', valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor, "Data", datetime.datetime.today()])
            return True

    def transferirValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Saldo insufiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['TRANSFERENCIA', valor, "Data", datetime.datetime.today()])
        return "Transferência Realizada"

    def gerarSaldo(self):
        print('Saldo da Conta')
        self.clientesConta()
        print(f'Numero: {self.numero} \nsaldo: R$ {self.saldo}')
