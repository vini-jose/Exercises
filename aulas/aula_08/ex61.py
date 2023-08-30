# Escreva um programa que peça ao usuário para digitar 
# um número inteiro e, em seguida, imprima o dobro desse número.
# Utilize try/excepet para lidar com a possibilidade de o 
# usuário inserir um valor não numérico
    
def main():
    while True:
        try:
            numero = int(input("Digite um número: "))
            dobro = numero*2
            print(f"O número é {numero} e o dobro dele é {dobro}")
            return numero
        except ValueError:
            print("Valor invalido")
            break
        
main()        
                 
        
        