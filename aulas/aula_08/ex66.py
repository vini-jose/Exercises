# Implemente uma função chamada "get_list_element" que 
# recebe uma lista e um índice como parâmetros. 
# A função deve retornar o elemento da lista no índice
# especificado. Caso o índice esteja fora do intervalo 
# válido, capture a exceção IndexError e retorne uma 
# mensagem indicando que o índice é inválido.

def get_list_element(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        return None

# Exemplo de uso:
minha_lista = [10, 20, 30, 40, 50]
indice = 2
resultado = get_list_element(minha_lista, indice)

if resultado is not None:
    print(f"O elemento no índice {indice} é: {resultado}")
else:
    print(f"Índice inválido! A lista não possui um elemento no índice {indice}.")