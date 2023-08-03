# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

produto = float(input("Escolha um produto: "))
valor = float(input("Qual o valor do produto: "))
pagamento = input(
    "Qual a forma de pagamento, à vista dinheiro/chegue, à vista no cartão, em até 2x no cartão e"
    "3x ou mais no cartão")

if pagamento == "à vista dinheiro/chegue":
    print(f"Você terá um desconto de 10% no produto: {valor-(valor*0.10)}")
elif pagamento == "à vista no cartão":
    print(f"Você terá um desconto de 5% no produto: {valor-(valor*0.5)}")
elif pagamento == "em até 2x no cartão":
    print(f"Você terá p preço formal: {valor}")
elif pagamento == " 3x no cartão" or "mais no cartão":
    print(f"Você terá 20% de juros: {(valor*0.20)+valor}")