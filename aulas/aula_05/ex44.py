# Monte um código para dizer se o numero informado é primo

cont = 0
n = int(input("Digite um valor: "))

if n > 1:
    for i in range(1, 11):
        if n % i == 0:
            cont += 1
    if cont > 2:
        print(f"Nâo é primo, ele é divisivel {cont} vezes")
    else:
        print(f"É primo, ele é divisivel apenas {cont} vez")
else:
    print("Não é primo")            