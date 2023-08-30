# Leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

import math

cat_op = float(input("Digite o comprimento do cateto oposto: "))
cat_ad = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cat_ad, cat_op)

print(f"O valor do cateto aposto é: {cat_op}")
print(f"O valor do cateto adjacente é: {cat_ad}")
print(f"O valor da hipotenusa é {hipotenusa}")