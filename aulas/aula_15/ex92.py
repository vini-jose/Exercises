# Desenvolva uma classe Rectangle com atributos width e height. Implemente um método calculate_area para calcular e retornar a área do retângulo.

class Rectangle:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        print(f"A area dos lados {self.base} e {self.altura} é: {area}")

base_1 = float(input("Digite a base de um retângulo: "))
altura_1 = float(input("Digite a altura do retângulo: "))

retangulo = Rectangle(base_1, altura_1)
retangulo.area()