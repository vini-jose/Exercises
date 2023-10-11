# Crie um script que permita o uso de 3 opções:
# Opções: A(Comprimento), B(Quantidade de espaços), C(soma dos números)

# Exemplo: "python main.py -o A/B/C -m 'mensagem'"
# Em que a 
# Opção A: retorne o tamanho/comprimento da mensagem
# Opção B: retorne a quantidade de espaços
# Opção C: retone a soma dos números fornecidos

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", choices=["A", "B", "C"], required=True, help="Escolha uma das opções A, B, C")
parser.add_argument("-m",help="Digite uma mensagem")

args = parser.parse_args()
opcao = args.o
mensagem = args.m

if opcao == "A":
    resultado = len(mensagem)
elif opcao == "B":
    resultado = mensagem.count("")
elif opcao == "C":
    resultado = sum(map(int, mensagem.split()))
else:
    print("Nenhuma opcão entre [A,B,C] escolhidas")

print(f"Opção {opcao} selecionada. Resultado: {resultado}")
