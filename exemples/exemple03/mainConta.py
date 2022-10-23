from EstacioParadigmasProgramacaoPython.exemples.exemple03.clientes import Clientes
from EstacioParadigmasProgramacaoPython.exemples.exemple03.conta import Conta

cliente01 = Clientes(123, "Juao", "Street of Road")
cliente02 = Clientes(456, "Mary", "Street off Road")

conta01 = Conta([cliente01, cliente02], 1, 100)

cliente01.infoCliente()
cliente02.infoCliente()

conta01.infoConta()
# conta01.gerarExtrato()
# conta01.depositar(1500)
# conta01.sacar(600)
# conta01.gerarExtrato()

#
# c1.infoConta()
# c2.infoConta()
#
# c1.transferirValor(c2, 500)
# c1.gerarExtrato()
# c2.gerarExtrato()
#
# c1.depostitar(300)
# saque = c1.sacar(100)
#
# c1.gerarExtrato()
# print(f'O saque foi realizado? {saque}')
#
# saque2 = c1.sacar(1300)
# print(f'O saque foi realizado? {saque2}')
