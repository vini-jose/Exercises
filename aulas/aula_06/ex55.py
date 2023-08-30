# Agora faça o exercício acima aceitar varios jogadores, inclua um sistema
# para visualizar detalhes do aproveitameto 

jogador = dict()
partida = list()
gol = list()

while True:
    jogador = input("Qual o nome do jogador?: ").upper()
    partida = int(input("Quantas partidas ele jogou?: "))
    gol = int(input("Quantos gols ele fez numa partida?: "))
    cont = input("Quer continuar? [S/N]: ").upper()
    if cont == "N":
        break
    
    
print(jogador)
print(partida)
print(gol)    
    