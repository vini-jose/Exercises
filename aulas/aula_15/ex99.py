# Crie uma classe Shape com um método abstrato calculate_area. Em seguida, defina classes derivadas Circle e Triangle 
# que herdam de Shape e implementam esse método para calcular suas respectivas áreas.

from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def calculando_area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    @classmethod
    def get(cls):
        raio = float(input("Digite os raio do circulo: "))
        return cls(raio)

    def calculando_area(self):
        return f"A área do circulo é: {math.pi * self.raio**2}"
    
    
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @classmethod
    def get(cls):
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        return cls(base, altura)

    def calculando_area(self):
        return f"A área do triângulo é: {(self.base * self.altura)/2}"
    
    
def main():        
    circulo_1 = Circulo.get()
    print(circulo_1.calculando_area())

    triangulo_1 = Triangulo.get()
    print(triangulo_1.calculando_area())
    
main()