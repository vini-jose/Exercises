# Defina uma classe BankAccount com atributos privados balance e account_number. Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, conta, saldo):
        self.conta = conta
        self.saldo = saldo

    def sal(self):
        return f"Na conta {self.conta} tem {self.saldo} reais de saldo"

    def sac(self): 
        sacar = input("O senhor quer fazer um saque? [S/N]: ").upper()

        if sacar == "S":
            quantidade = int(input("Qual o valor que o senhor vai sacar: "))
            if quantidade <= self.saldo:
                saldo_atual = self.saldo - quantidade
                print(f"O senhor sacau {quantidade}R$ e seu saldo ficou {saldo_atual}R$")
            else:
                print("O senhor não tem saldo")
        else:
            print("Ok, posso ajudar em outra coisa?")
            
    def dep(self):
        depositar = input("O senhor quer fazer um deposito? [S/N]: ").upper()

        if depositar == "S":
            quantidade =  int(input("Qual o valor que o senhor vai depositar: "))
            if quantidade >= 1:
                saldo_atual = self.saldo + quantidade
                print(f"O senhor depositou {quantidade}R$ e seu saldo ficou {saldo_atual}R$")
            else:
                print("O senhor tem que depositar um valor igual ou maior que 1R$")
        else:
            print("Ok, posso ajudar em outra coisa?")

conta_1 = BankAccount(1, 100)
conta_1.sac()
conta_1.dep()