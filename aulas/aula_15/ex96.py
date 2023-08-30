# Crie uma classe Employee com atributos name, position e salary. 
# Adicione um método apply_raise que aumenta o salário do 
# funcionário em uma determinada porcentagem.

class Funcionario: 
    def __init__(self, nome, posicao, salario):
        self.nome = nome
        self.posicao = posicao
        self.salario = salario

    def aumento(self):
        aumento_salario = self.salario * 0.1
        salario = self.salario + aumento_salario
        print(f"Você tinha o salário {self.salario} e teve um aumento de 10%, seu salari ficou {salario}")

nome_1 = input("Digite seu nome: ")
cargo_1 = input("Digite seu cargo: ")
salario_1 = int(input("Digite seu salario: "))

salario = Funcionario(nome_1, cargo_1, salario_1)
salario.aumento()