# 1. Crie uma função que receba um número como parametro e retorne o seu quadrado. Por exemplo, se a função for chamada de quadrado,
# chamar quadrado(2) deve retornar 4.


def main():
    numero = quadrado()
    print(f"o quadrado do número é {numero}")

def numero():
    return int(input("Digite um número: "))

def quadrado():
    x = numero()
    x = x**2
    return x

main()