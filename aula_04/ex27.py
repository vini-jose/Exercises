# Faça um programa que leia 3 retas do usuario e diga se elas podem 
# formar um triangulo

r1 = input("Digite o valor de uma reta: ")
r2 = input("Digite o valor de outra reta: ")
r3 = input("Digite o valor de outra reta: ")

print(f"As retas que você escolheu é: {r1, r2, r3}")
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas acimas podem formar um triangulo")
else:
    print("As retas não podem formar um triangulo") 