# A Confederação Nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JUNIOR
#- Até 25 anos: SÉNIOR
#- Acima de 25 anos: MASTER

ano = float(input("Qual o ano do seu nascimento: "))
idade = (2023-ano)

print(f"Sua idade é: {idade}")
if idade <= 9:
    print("Você está na categoria mirim")
elif idade <=14:
    print("Você está na categoria infantil")
elif idade <= 19:
    print("Você está na categoria junior")
elif idade <= 25:
    print("Você está na categoria sénior")
elif idade > 25:
    print("Você está na categoria master")