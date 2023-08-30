# Mostre o  fatorial de um numero enviado pelo usuario
# ex: 5x4x2x1 = 120

num = int(input("Descubra o fatorial de um número: \n"))
counter = num
fat = 1

print(f"Calculando {num}! = ", end="")
while counter > 0:
    print("{}".format(counter), end="")
    fat *= counter
    counter -= 1
    print(" x " if counter > 1 else " = ", end="")
print(f"{fat}")