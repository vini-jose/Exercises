# Desenvolva um programa que calcule a soma de todos números
# mutiplos de três entre 1 e 500
# e mostre quantos numeros são divisiveis

soma = 0
divisiveis = 0

for i in range(1, 501):
    if i % 3 == 0:
        soma += i
        divisiveis += 1
print(f"Soma dos divisores: {soma}")
print(f"A quantidade de números divisiveis: {divisiveis}")


        
        
   
            