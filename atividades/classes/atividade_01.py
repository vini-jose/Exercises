# Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        
    def mostrar_cor(self):
        return self.cor
    
minha_bola = Bola("Azul", 10, "Borracha")
print(minha_bola.mostrar_cor())

minha_bola.trocar_cor("vermelho")
print(minha_bola.mostrar_cor())