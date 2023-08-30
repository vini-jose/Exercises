# Refaça o desafio de PA mostrando os 20 primeiros termos 
# e pergunte ao usuario quantos termos a mais ele quer ver 
# o programa encerra quando disser que quer mostrar 0 termos

n = int(1)
n1 = int(11)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A.: '))

while n < n1:
    termo = primeiro + (n - 1 )* razao
    print (termo, end= ', ')
    n += 1  
    if n == n1:
        print('Pause')
        n1 += int(input("Quantos termos a mais deseja visualizar? "))
        continue
    elif (n1 == 0):
        break
print(f'Programa encerrado, com {n} termos mostrados')

     
    