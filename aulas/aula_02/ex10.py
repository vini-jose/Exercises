# Faça um programa que leia a altura e largura de uma parede e calcule
# sua area, mostre quantos litros de tinta sera necesseario para pintar
# sabendo que 1L pinta 2m quadrados

altura = float(input("Qual a altura da sua parede em metros? "))
largura = float(input("Qual a largura da sua parede? "))
area = altura*largura

print(f"A area da sua parede é {area}, você iria precisar de {area/2} litros para pintar sua parede")
