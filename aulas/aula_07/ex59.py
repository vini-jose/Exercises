# Desenvolva uma função que verifique se uma palavra é um palíndromo (ou
# seja, lida da mesma forma da esquerda para a direita e vice-versa).
# A função deve retornar True se a palavra for um palíndromo e False caso
# contrário.

def verifica_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    
    if palavra_invertida == palavra:
        return print("True")        
    else:
        return print("False")
    
verifica_palindromo("ata")