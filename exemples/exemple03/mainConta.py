from EstacioParadigmasProgramacaoPython.exemples.exemple03.conta import Conta

c1 = Conta(1, 1, "Juao", 1000)
print(f"Nome do Titular da conta: {c1.nomeTitular}")
print(f"Número da conta: {c1.numero}")
print(f"CPF do titular da conta: {c1.cpf}")
print(f"Saldo da Conta: R$ {c1.saldo}")
c1.depostitar(300)
saque = c1.sacar(100)

c1.gerarExtrato()
print(f'O saque foi realizado? {saque}')

saque2 = c1.sacar(1300)
print(f'O saque foi realizado? {saque2}')

