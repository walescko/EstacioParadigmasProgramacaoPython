class Conta:
    def __init__(self,numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depostitar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerarExtrato(self):
        print('Saldo da Conta')
        print(f'numero: {self.numero} \ncpf: {self.cpf} \nsaldo: R$ {self.saldo}')



