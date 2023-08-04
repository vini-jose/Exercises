# Classe "Circulo"
# Crie uma classe chamada "Circulo" que possua o método __init__
# para inicializar a propriedade "raio" do circulo
# Em seguifa, crie um objeto da classe "Circulo" e calcule e
# imprima a àrea do circulo



class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
def circul0():
    print(circulo())
        
def raio():
    return float(input("Digite o valor do raio do circulo: "))

def circulo():
    area = raio()**2 * 3.14
    print(f"A àrea do circulo é {area}")

circulo()
    