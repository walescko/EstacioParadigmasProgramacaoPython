class Clientes:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    def infoCliente(self):
        print(f'Cliente: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Endereço {self.endereco}')
