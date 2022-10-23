# Classe Salário
class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus
    def salarioAnual(self):
        return (self.base*12)+self.bonus
