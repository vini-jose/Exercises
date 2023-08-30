# Crie uma função chamada "recursive_factorial" que calcula 
# o fatorial de um número de forma recursiva.
# Utilize try/except para verificar se o argumento passado 
# é um número inteiro não negativo e lidar com outras 
# exceções que possam surgir durante a recursão 

def main():
    num = input("Digite um número inteiro não negativo: ")

    try:
        num = int(num)
        result = recursive_factorial(num)
        print(f"O fatorial de {num} é {result}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro não negativo.")

def recursive_factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("O argumento deve ser um número inteiro não negativo.")
        
        if n == 0 or n == 1:
            return 1
        else:
            return n * recursive_factorial(n - 1)
    
    except ValueError as ve:
        return str(ve)
    except RecursionError:
        return "Ocorreu um erro de recursão. Certifique-se de que o número não seja muito grande."
    except Exception as e:
        return "Ocorreu um erro durante o cálculo do fatorial: " + str(e)

main()