# Crie uma função chamada "read_file" que recebe o nome de
# um arquivo e tenta abri_lo para leitura
# Se o arquivo não existir , capture a exceção
# FileNotFoundError e imprima uma mensagem amigavel para o
# usuário

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"O arquivo {file_name} não foi encontrado.")
    except IOError:
        print(f"Erro ao ler o arquivo {file_name}.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Exemplo de uso da função:
file_name = "exercises/aula_08/texto.txt"
file_content = read_file(file_name)

if file_content is not None:
    print("Conteúdo do arquivo:")
    print(file_content)
