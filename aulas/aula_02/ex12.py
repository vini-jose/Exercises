# Calcule um aumento de 15% no salário de um funcionário

nome = input("Qual seu nome? ")
salario_antigo= float(input("Qual a seu salário? "))
salario_novo = salario_antigo*0.5

print(f"{nome} ganhava R${salario_antigo}")
print(f"{nome} teve um aumento de 15% e ficou com: R${salario_novo + salario_antigo}")