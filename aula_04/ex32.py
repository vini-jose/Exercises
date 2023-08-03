# Crie um rpograma que leia duas notas dde um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atigida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÂO
#- Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1+nota2)/2

print(f"Sua média é: {media}")
if media >= 7:
    print("APROVADO")
elif 6.9 >= media >=5:
    print("RECUPERAÇÂO")
elif media < 5:
    print("REPROVADO") 

