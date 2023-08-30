# Crie um programa que solicite ao usuário que digite um 
# valor numérico inteiro. Em seguida, tente encontrar o 
# fatorial desse número. Utilize try/except para tratar a
# Inserção de valores não inteiros e números negativos

def numero_fatorial():
    try:
        numero = int(input("Digite um número: "))
        fatorial = 1
        if numero > 0:
            for c in range(1, numero+1):
                fatorial *= c
            print(fatorial) 
        else:    
            raise ValueError("Não é possível calcular com o número negativo.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, tente novamente.")

numero_fatorial()

