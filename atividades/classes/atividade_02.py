# Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mostrar_valor(self):
        return self.lado
        
    def mudar_valor_do_lado(self, novo_lado):
        self.lado = novo_lado
    
    def retornar_valor_do_lado(self):
        return self.lado
        
    def area(self):
        return self.lado ** 2
    
lado_do_quadrado = Quadrado(2)
print(lado_do_quadrado.mostrar_valor())

lado_do_quadrado.mudar_valor_do_lado(4)
print(lado_do_quadrado.retornar_valor_do_lado())

print(f"A area do quadrado é: {lado_do_quadrado.area()}")