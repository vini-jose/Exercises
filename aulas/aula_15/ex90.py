# Crie uma classe chamada Person com atributos name e age, e um método display_info que imprime o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir_info(self):
        print(F"Seu nome é {self.nome} e sua idade é {self.idade}")     
    
pessoa = Pessoa("José", 19)

pessoa.imprimir_info()
