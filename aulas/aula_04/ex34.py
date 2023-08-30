# Refaça o DESAFIO 027 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado
#- EQUILÁTERO: todos od lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

r1 = input("Digite o valor de uma reta: ")
r2 = input("Digite o valor de outra reta: ")
r3 = input("Digite o valor de outra reta: ")

print(f"As retas que você escolheu é: {r1, r2, r3}")
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas acimas podem formar um triangulo")
    if r1 == r2 == r3:
        print("Equilatero")
    elif r1 != r2 != r3:
        print("Escaleno")
    else:
        print("Isósceles") 
else:
    print("As retas não podem formar um triangulo") 
