class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroConta):
        print(f'Extrato : {numeroConta} \n')
        for i in self.transacoes:
            print(f"{i[0]:15s} {i[1]:10.2f} {i[2]:10s} {i[3].strftime('%d/%m/%y')}")
