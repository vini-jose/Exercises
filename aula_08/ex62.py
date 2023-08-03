# Crie uma função chmada "divide_numbers" que recebe dois
# parâmetros numéricos (a e b) e retorne a divisão de a por b.
# Utilize try/except para tratar a divisão por zero
    
def divide_numero():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))          
    resultado = n1/n2
    while True:
        try:
            print(resultado)
            return resultado
        except ZeroDivisionError:
            print("Digite outro valor")

divide_numero()        