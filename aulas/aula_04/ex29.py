# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão
# 1 para binário, 2 para octal e 3 para hexadecimal

numero = int(input("Digite um número: "))
base = int(input("Escolha a base de conversão 1 = a binário, 2 = octal, 3 para hexadecimal: "))

if base == 1:
    print(f"{bin(numero)}")
elif base == 2:
    print(f"{oct(numero)}")
elif base == 3:
    print(f"{hex(numero)}")
    
    
    
    