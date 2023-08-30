# Gerencie um jogador de futebol lendo o nome e quantas partidas ele jogou
# Depois, leia a quantidade de gols feitas em cada partida
# Coloque tudo num dicionário incluindo o total de gols durante o periodo

def gerenciar_jogador():
    nome_jogador = input("Digite o nome do jogador: ")
    num_partidas = int(input("Digite a quantidade de partidas que o jogador jogou: "))

    gols_por_partida = []
    total_gols = 0

    for partida in range(1, num_partidas + 1):
        gols_partida = int(input(f"Digite a quantidade de gols feitos na partida {partida}: "))
        gols_por_partida.append(gols_partida)
        total_gols += gols_partida

    jogador = {
        'Nome': nome_jogador,
        'Partidas': num_partidas,
        'Gols por partida': gols_por_partida,
        'Total de gols': total_gols
    }

    return jogador

jogador_info = gerenciar_jogador()
print(jogador_info)

    
