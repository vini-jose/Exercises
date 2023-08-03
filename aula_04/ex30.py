# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguals

n1 = int(input("Escolha um número: "))
n2 = int(input("Escolha outro número: "))

print(f"Os números ecolhidos foram {n1} e {n2}")
if n1 > n2:
    print("O primeiro valor é maior")
elif n2 > n1:
    print("O segundo é maior")
else:
    print("Não existe valor maior, os dois são iguais")