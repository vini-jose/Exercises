# Classe "Retângulo":
# Crie uma classe chamada "Retângulo" que possuea o método 
# __init__ para inicializar as propriedades "largura" e "altura"
# do retângulo. Em seguida, crie um objeto da classe "Retângulo"
# e calcule e imprima a área do retângulo.

class Retangulo:
    def __init__(self, largura, altura, raiz):
        self.largura = largura
        self.altura = altura
        self.raiz = raiz
        
        
def main():
    rentagulo = get_retangulo()
    print(f"O Retângulo tem {rentagulo.altura} altura, {rentagulo.largura} largura e a raiz dele é {rentagulo.raiz} ")
    
def get_retangulo():
    altura = float(input("Qual a altura do retângulo: "))
    largura = float(input("Qual a largura do triângulo: "))
    raiz = largura*altura
    return Retangulo(altura, largura, raiz)

main()
        