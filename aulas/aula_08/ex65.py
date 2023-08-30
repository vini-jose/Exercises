# Escreva um programa que leia um valor numérico inteiro 
# do usuário e imprima o resultado da raiz quadrada desse
# valor. Utilize try/except para lidar com a possibilidade 
# de p usuário inserir um número negativo.

import math

def calcular_raiz_quadrada():
    while True:
        try:
            valor = int(input("Digite um valor inteiro: "))
            if valor < 0:
                raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
            resultado = math.sqrt(valor)
            print(f"A raiz quadrada de {valor} é: {resultado:.2f}")
            return resultado
        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")

calcular_raiz_quadrada()