# Leia o peso de 5 pessoas e mostre o maior e o menor peso digitado


lista = []  
for c in range(1, 6):
    peso = float(input("Qual seu peso: "))
    lista += [peso]   
print('')
print(f"O Maior peso foi: {max(lista)}")  
print(f"O Menor peso foi: {min(lista)}")  