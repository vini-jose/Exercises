# Exercícios Mais Complexos:

# Desenvolva uma classe Bank que gerencia várias contas bancárias. Os métodos devem permitir criar novas contas, 
# fazer transferências entre contas e calcular o saldo total do banco.

class Bank:
    def __init__(self):
        self.conta = []
        self.saldo = []

    def add_conta(self, contas):
        self.conta.append(contas)

    def criar_conta(self):
        for contas in range(0, 2):
            conta = int(input("Escreva sua conta: "))
            

