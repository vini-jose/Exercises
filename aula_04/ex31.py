# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Qual o ano o seu nascimento?: "))
idade = 2023-ano

if idade < 18:
    print("Você ainda vai se alistar")
    print(f"Falta {18-idade} para se alistar")
elif idade == 18:
    print("É a hora exata de se alistar")
else:
    print("Já passou do tempo para se alistar")
    print(f"Passou {idade-18} para se alistar")
    