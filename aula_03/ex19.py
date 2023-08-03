# Agora, sorteie uma ordem aleatória de 4 alunos. Leia o nome 
# dos alunos e mostre a ordem aleatória

import random

aluno1 = (input("Digite nome de um aluno: "))
aluno2 = (input("Digite nome de um aluno: "))
aluno3 = (input("Digite nome de um aluno: "))
aluno4 = (input("Digite nome de um aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

print(f"Lista de alunos: {lista}")
random.shuffle(lista)
print("Lista em ordem aleatoria", (lista))

