# Faça um programa que leia a quilometragem de um carro, caso esteja
# acima dos 80km/h, multe o carro

km = int(input("Qual a quilometragem que o carro passou: "))

print(f"A quilometragem do carro é: {km}km/h")
if km > 80:
    print("Você levou uma multa")
else:
    print("Você não foi multado")