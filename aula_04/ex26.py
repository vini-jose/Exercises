# Escreva um codigo que pergunte o salário de um funcionario e de um aumento
# de 15% caso o salário for maior que 1250 reais, caso contrario 10%

salario = float(input("Qual seu salário?: "))
maior = salario*0.15
menor = salario*0.1

print(f"Seu salário era: R${salario}")
if salario > 1250:
    print(f"Vc teve um aumento de 15%, que teria um aumento de R${maior}")
    print(f"Seu salário ficaria R${salario+maior}")
else:
    print(f"Você teve um aumento de 10%, que teria um aumento de R${menor}")
    print(f"Seu salário ficaria R${salario+menor}")