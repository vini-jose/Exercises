#3. Crie uma função que receba uma string como parametro e retorne a string invertida. Por exemplo, se a função for chamada de
#inverter_string, chamar inverter_string("olá") deve retornar "álO"

def inverter_palavra():
    palavra = input("Digite seu nome: ")
    palavra_invertida = palavra[::-1]
    return palavra_invertida

def imprimir_palavra_invertida():
    palavra_invertida = inverter_palavra()
    print(palavra_invertida)
    
imprimir_palavra_invertida()