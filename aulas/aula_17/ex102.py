# Faça um script que permita o uso de 2 argparsers ("age", "city")
# Se for passado idade/cidade então printe na tela o valor. Se não, printe
# "Nenhuma mensagem fornecida"

import argparse

parser = argparse.ArgumentParser(description="Chamando a idade e a cidade da pessoa")
parser.add_argument("-i", type=int, help="Idade a ser exibida")
parser.add_argument("-c", help="Cidade a ser exibida")

args = parser.parse_args()
idade = args.i
cidade = args.c

if idade and cidade:
    print(f"Idade: {idade}\nCidade: {cidade}")
else:
    print("Nenhuma informação fornecida.")
