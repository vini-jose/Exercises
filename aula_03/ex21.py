# Crie um jogo que faça o computador pensar em um número de 0 a 5 e 
# permita o usuario ter um chute para acertar

import random

lista = [0, 1, 2, 3, 4, 5]
numero = int(input("Digite um numero de 0 a 5: "))
sorteado = (random.choice(lista))

print(f"O numero que você escolheu é: {numero}")
print(f"O numero sorteado é: {sorteado}")

if numero == sorteado:
    print("Você acertou")
else: 
    print("Você errou")
