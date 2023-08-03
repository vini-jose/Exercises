# Escreva um programa que peça ao usuário para digitar 
# um número inteiro e, em seguida, imprima o dobro desse número.
# Utilize try/excepet para lidar com a possibilidade de o 
# usuário inserir um valor não numérico
    
def main():
    n = get_int()
    dobro = n*2
    print(f"O número é {n} e o dobro dele é {dobro}")




def get_int():
    while True:
        try:
            return int(input("Digite um número: "))        
        except ValueError:
            print("Valor invalido")
        
main()        
                 
        
        