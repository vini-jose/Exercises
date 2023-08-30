# Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base=0, altura=0):
        self.base = base
        self.altura = altura
    
    def mostrar_valor(self):
        return self.base, self.altura
      
    def mudar_valor(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura
        
    def retornar_valor(self):
        return self.base, self.altura
        
    def area(self):
        return self.base * self.altura
        
        
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
base_1 = float(input("Informe a base do local: "))
altura_1 = float(input("Informe a altura do local: "))
piso = float(input("Digite o tamanho do piso: "))
rodape = float(input("Digite o tamanho do rodape: "))

medidas = Retangulo(base_1, altura_1)
print(medidas.mostrar_valor())

medidas.mudar_valor(24, 12)

area_local = medidas.area()
perimetro_local = medidas.perimetro()

quantidade_pisos = area_local / piso
quantidade_rodapes = perimetro_local / rodape

print("Quantidade de pisos necessários:", quantidade_pisos)
print("Quantidade de rodapés necessários:", quantidade_rodapes)