# Defina uma classe Car com atributos make, model e year. Crie um método start_engine 
# que imprime uma mensagem indicando que o motor foi iniciado.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def start_engine(self):
        print(f"O Motor do carro {self.marca} do modelo {self.modelo} do ano {self.ano} foi iniciado")
    
marca_1 = input("Digite a marca do seu carro: ")
modelo_1 = input("Digite o modelo do carro: ")
ano_1 = input("Digite o anno do carro: ")

carro = Carro(marca_1, modelo_1, ano_1)
carro.start_engine()