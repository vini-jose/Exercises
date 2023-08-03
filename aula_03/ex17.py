# Leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosseno e tangente desse ângulo

import math

angulo = float(input("Digite um ângulo qualquer: "))


seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tagente =  math.tan(math.radians(angulo))

print(f"O valor do ângulo é: {angulo}")
print(f"O valor do seno é: {seno}")
print(f"O valro do cosseno é: {cosseno}")
print(f"O valor da tagente é: {tagente}")