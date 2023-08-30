# Crie um programa onde 4 jogadores jogam um dado 
# Guarde esses resultados em um dicionário
# No final, coloque esse dicionário em ordem (do maior para o menor)

from random import randint

d1 = {}

for c in range(0, 4):
    nome = str(input("Digite um nome: "))
    dado = randint(0, 6)
    d1[nome] = dado
    
d1 = dict(sorted(d1.items(), key=lambda item: item[1], reverse=True))
    
print("Resultados dos jogadores em ordem de maior para menor:")
for jogador, resultado in d1.items():
    print(f"{jogador}: {resultado}")




















    




