# Faça um programa que leia 3 valores e diga o maior e menor valor 

print("Digite 3 numeros diferentes")
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
valor3 = int(input("Digite outro valor: "))

print(f"Os numeros escolhidos são: {valor1, valor2, valor3}")

# Código do primeiro valor
if valor1 > valor2 and valor1 > valor3:
    print(f"O numero {valor1} é maior")
elif valor1 < valor2 and valor1 < valor3:
    print(f"O numero {valor1} é menor")
else:
    print(f"O numero {valor1} é o do meio")

# Código do segundo valor    
if valor2 > valor1 and valor2 > valor3:
    print(f"O numero {valor2} é maior")
elif valor2 < valor1 and valor2 < valor3:
    print(f"O numero {valor2} é menor")
else:
    print(f"O numero {valor2} é o do meio")

# Código do terceiro valor    
if valor3 > valor1 and valor3 > valor2:
    print(f"O numero {valor3} é maior")
elif valor3 < valor1 and valor3 < valor2:
    print(f"O numero {valor3} é menor")
else:
    print(f"O numero {valor3} é o do meio")
    
        