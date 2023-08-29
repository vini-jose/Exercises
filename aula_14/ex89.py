# Bank Account. Crie uma classe "BankAccount" que inicialize com 
# "account_number" e "balance". Depois crie um método para sacar e
# outro para depositar. Após isso, teste criando 2 objetos em que um saca
# e o outro deposita certos valores. No fim, mostre a mudança na tela.

class BankAccount:
    def __init__(self, numero_da_conta, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def sal(self):
        return f"Na conta {self.numero_da_conta} tem {self.saldo} reais de saldo"

    def sac(self, sacar):
        if sacar <= self.saldo:
            return self.saldo - sacar 
        else: 
            print("Você não tem esse saldo disponivel")
         
    def dep(self, depositar):
         if depositar >= 1:
             return self.saldo + depositar 
         else: 
             print("Deposite um valor igual ou maior que 1 real")

conta_1 = BankAccount(1, 100)
conta_2 = BankAccount(numero_da_conta= 2)

print(f"A conta {conta_1} fez o deposito e tem o saldo de: {conta_1.dep(500)}")
print(f"A conta {conta_2} fez o saque e tem o saldo de: {conta_2.sac(200)}")
