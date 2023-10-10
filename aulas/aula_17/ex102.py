# Faça um script que permita o uso de 2 argparsers ("age", "city")
# Se for passado idade/cidade então printe na tela o valor. Se não, printe
# "Nenhuma mensagem fornecida"

import argparse

def pedindo_a_idade(idade, cidade):
    if idade:
        print(f"Idade: {idade}\nCidade: {cidade}")
    if not idade and not cidade:
        print("Nenhuma informação fornecida.")


parser = argparse.ArgumentParser(description="Chamando a idade e a cidade da pessoa")
parser.add_argument("--idade", type=int, help="Idade a ser exibida")
parser.add_argument("--cidade", help="Cidade a ser exibida")

args = parser.parse_args()
idade = args.idade
cidade = args.cidade

pedindo_a_idade(idade, cidade)