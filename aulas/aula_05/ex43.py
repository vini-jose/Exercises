# Leia o primeiro termo e a razão de uma PA. Depois, mostre
# os 20 primeiros termos

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
vigesimo = primeiro + (20 - 1) * razao

for c in range(primeiro, vigesimo, razao):
    print(f"{c}", end=",")
print("Acabou")