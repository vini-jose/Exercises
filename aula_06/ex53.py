# Crie um dicionário que guarde o nome, ano de nascimento a idade
# o ano de contrato e o salario de um funcionario 
# Calcule e acrescente no dicionario quantos anos a pessoa aposentará

from datetime import datetime

def calcular_ano_aposentadoria(ano_nascimento, ano_contrato):
    idade_contrato = ano_contrato - ano_nascimento
    idade_aposentadoria = 65   # Idade de aposentadoria padrão (você pode ajustar esse valor se necessário)
    ano_aposentadoria = ano_contrato + (idade_aposentadoria - idade_contrato)
    return ano_aposentadoria

funcionario = {}

funcionario["nome"] = input("Qual seu nome?: ").upper()
funcionario["ano_nascimento"] = int(input("Qual o ano do seu nascimento?: "))
funcionario["idade"] = int(input("Qual a sua idade?: "))
funcionario["ano_contrato"] = int(input("Ano de contrato?: "))
funcionario["salario"] = float(input("Qual seu salário?: "))

funcionario["ano_aposentadoria"] = calcular_ano_aposentadoria(funcionario["ano_nascimento"], funcionario["ano_contrato"])
funcionario["idade_aposentadoria"] = funcionario["ano_aposentadoria"] - datetime.now().year

print("\nInformações da Pessoa:")
for chave, valor in funcionario.items():
    print(chave + ":", valor)