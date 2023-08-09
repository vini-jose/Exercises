# 3. Crie uma função que receba uma string como parametro e retorne a string invertida. Por exemplo, se a função for chamada de
#inverter_string, chamar inverter_string("olá") deve retornar "álO"

def inverter_palavra():
    palavra = input("Digite seu nome: ")
    palavra_invertida = palavra[::-1]
    print(palavra_invertida)
    return palavra_invertida

inverter_palavra()