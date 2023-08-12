# Crie uma função que receba uma lista de números como entrada e retorne
# o maior número presente na lista.

lista = [3, 5, 7, 88]

def get_lista():
    numero = lista
    maior = sorted(numero, reverse=True)
    print(f"O número maior é {maior[0]}")

get_lista()