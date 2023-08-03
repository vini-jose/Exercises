# Melhore o jogo de adivinhação onde o computador "pensa" 
# em um número. Mostre quantos palpites o usuario usou

import random

computador = random.randint(1, 5)
palpite = 0


print("Regras")
print("Digite um número de 1 a 5")

while True:
    resposta = int(input("Digite o número: "))    
    if computador == resposta:
        print("Você acertou")
        palpite += 1        
    else:
        print("Você errou")
        palpite += 1
    if computador == resposta:
        break

print(f"Você teve {palpite} palpites")
 