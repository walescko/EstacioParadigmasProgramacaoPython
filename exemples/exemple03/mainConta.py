from EstacioParadigmasProgramacaoPython.exemples.exemple03.conta import Conta

c1 = Conta(1, 1, "Juao", 1000)
c2 = Conta(2, 2, 'Mary', 500)

c1.infoConta()
c2.infoConta()

c1.depostitar(300)
saque = c1.sacar(100)

c1.gerarExtrato()
print(f'O saque foi realizado? {saque}')

saque2 = c1.sacar(1300)
print(f'O saque foi realizado? {saque2}')

