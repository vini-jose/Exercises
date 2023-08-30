# Desenvolva uma mini calculadora em que seja permitido:
# somar, mutiplicar, maior, novos numeros e sair

n1 = float(input("Escolha o primeiro número para botar na calculadora: "))
n2 = float(input("Escolha o segundo número para botar na calculadora: "))

soma = (n1 + n2) 
divisao = (n1/n2)

while True:
    print(f"A soma dos números {n1} e {n2} é: {soma}")
    print(f"A divisão dos valores {n1} e {n2} é: {divisao}")
    if n1 > n2:
        print(f"O primeiro número é maior, que é: {n1}")
    elif n1 == n2:
        print("Os números são iguais")
    else:
        print(f"O segundo número é maior, que é: {n2}")
    if n1 > n2 or n1 < n2 or n1 == n2:
        n3 = float(input("Escolhas outro número: "))
        n4 = float(input("Escolha outro números: "))
        break
    
           