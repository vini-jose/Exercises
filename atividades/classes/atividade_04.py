# Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    @classmethod   
    def criar_pessoa(cls):
        nome = input("Qual seu nome? ")
        idade = int(input("Qual sua idade? "))
        peso = float(input("Qual seu peso? "))
        altura = float(input("Qual sua altura? "))
        return cls(nome, idade, peso, altura)
    
    def envelhecer(self):
        aumentar = 18
        self.idade += aumentar
        return f"Você envelheceu {aumentar} e sua idade atual é {self.idade}"
        
    def engordar(self):
        aumentar = 5.5
        self.peso += aumentar
        return f"Você engordou {aumentar} quilos e seu peso atual é {self.peso}"
        
    def emagrecer(self):
        diminuir = 1.0
        self.peso -= diminuir
        return f"Você emagreceu {diminuir} e seu peso atual é {self.peso}"
        
    def crescer(self):
        aumentar = 0.15
        self.altura += aumentar
        return f"Você cresceu {aumentar} centímetros e sua altura atual é {self.altura}"
    
def main():
    jose = Pessoa.criar_pessoa()
    print("Nome:", jose.nome)
    print("Idade:", jose.idade)
    print("Peso:", jose.peso)
    print("Altura:", jose.altura)
    print(jose.envelhecer())
    print(jose.engordar())
    print(jose.emagrecer())
    print(jose.crescer())
    
main()