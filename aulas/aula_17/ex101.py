# Crie um programa para rodar "python main.py --nome (nome)" e que o
# argumento seja obrigatório (ou requerido)

import argparse

parser = argparse.ArgumentParser(description="Chamando o nome de alguém")
parser.add_argument("--nome", required=True, help="Nome a ser exibido")

args = parser.parse_args()
nome = args.nome

print(nome)