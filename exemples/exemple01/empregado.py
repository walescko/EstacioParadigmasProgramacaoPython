#Classe Empregado
class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salarioAgregado = salario
    def salarioTotal(self):
        return self.salarioAgregado.salarioAnual()