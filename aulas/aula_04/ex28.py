# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# a prestação mensal não pode exceder 30% do salário ou o emprestimo será negado

casa = float(input("Qual o valor da casa que você está interessado?: "))
salario = float(input("Quanto é o seu salário?: "))
pagamento = int(input("Quantos anos você irá pagar o emprestimo?: "))

credito_maximo = salario*0.3
parcela_anual = casa/pagamento
parcela_mensal = parcela_anual/12

if parcela_mensal <= credito_maximo:
    print("Seu emprestimo foi aceito")
else:
    print("Seu emprestimo foi negado")
    