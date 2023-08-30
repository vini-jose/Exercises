# Escreva um programa que solicite ao usuário que insira o
# nome de um arquivo e uma palavra aparece no arquivo e exibir o 
# resultado. Utilize try/except para lidar com a possibilidade 
# de o arquivo não existir ou encontrar um erro de leitura

def main():
    file_name = input("Digite o nome do arquivo: ")

    try:
        with open(file_name, 'r') as file:
            content = file.read()

        word_to_find = input("Digite a palavra a ser procurada no arquivo: ")
        word_count = count_word_occurrences(content, word_to_find)

        print(f"A palavra '{word_to_find}' aparece {word_count} vezes no arquivo.")

    except FileNotFoundError:
        print(f"O arquivo '{file_name}' não foi encontrado.")
    

def count_word_occurrences(content, word_to_find):
    return content.count(word_to_find)        
        

if __name__ == "__main__":
    main()