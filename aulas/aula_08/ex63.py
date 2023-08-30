# Escreva um programa que solicite ao usuário que digite seu
# nome e sua idade. Em seguida, tente converter a idadde em
# um número inteiro. Se a conversão falhar, informe ao usúario
# que a idade digitada é invalida e continue o programa
# Caso contrario, exiba uma mensagem com o nome e a idade

def obter_nome_e_idade():
    nome = input("Digite seu nome: ")
    idade_str = input("Digite sua idade: ")

    try:
        idade = int(idade_str)
        print(f"Seu nome é {nome} e você tem {idade} anos.")
    except ValueError:
        print("Idade inválida. Certifique-se de digitar um número inteiro para a idade.")
        obter_nome_e_idade() 


obter_nome_e_idade()
