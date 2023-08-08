# 2. Crie uma função que receba dois números como parametro e retorne a soma deles. Por exemplo, se a função for chamada de adicionar,
# chamar adicionar(1,2) deve retornar 3. 

def adicionar():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    soma = num1 + num2
    print(f"A soma dos números {num1} e {num2} é {soma}")


adicionar()