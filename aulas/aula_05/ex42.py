# Crie um programa que receba 5 valores int e no final mostre
# a soma apenas dos pares

soma = 0

print("Escolha cincos números")
for c in range(0, 5):
    num = int(input("Digite um número: "))
    if num % 2 ==0:
        soma += num
        print(f"A soma dos pares é {soma}")
    