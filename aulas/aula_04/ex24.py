# Faça um programa que leia a distancia em km de uma viagem, se 
# a distancia for menor ou igual a 200km cobre 50 centavos por km rodado,
# caso contrário cobre 45 centavos.

km = float(input("Quantos quilometros pecorreu na viagem em km: "))

print(f"Sua distancia é: {km}km")
if km <= 200:
    print(f"A sua distancia foi menor ou igual a 200km, você ira cobrir R$0.50 e sera cobrado: R${km*0.50}")
else:
    print(f"A distancia foi maior que 200km, você Ira cobrir R$0.45 e sera cobrado: R${km*0.45}")
