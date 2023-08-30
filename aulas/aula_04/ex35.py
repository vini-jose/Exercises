# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa corporal (IMC) e mostre seu status,
# de acrodo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input("Quantos quilos você pesa: "))
altura = float(input("Qual a sua altura: "))
imc = peso/altura**2

print(f"Seu imc é: {imc}")

if imc < 18.5:
    print("Abaixo do Peso")
elif 18.5 == imc <= 25:
    print("Peso Ideal") 
elif 25 <= imc <=30:
    print("Sobrepeso")
elif 30 <= imc <=40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade Mórbida")
