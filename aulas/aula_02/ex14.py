# Faça um programa que leia a quantidade de dias e km rodados por um  carro
# alugado, depois calcule o valor do contrato sabando que:
# cada dia custa 60 reais e cada km custa 15 centavos

modelo = input("Qual é o modelo do carro? ")
dia = int(input("Quantos dias o carro rodou? "))
km = float(input("Quantos km o carro rodou? "))
valor_dia = dia*60
valor_km = km*0.15 

print(f"O valor em dias para pagar é: R${valor_dia}")
print(f"O valor em quilometragem para pagar é: R${valor_km}")
print(f"O valor do contrato para pagar é: R${valor_dia + valor_km}")