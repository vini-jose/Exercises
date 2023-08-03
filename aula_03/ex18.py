# Faça um programa que leia o nome de 4 alunos e escreva na tela 
# o nome do escolhido para apagar o quadro

import random

aluno1 = str(input("Escreva o nome de um aluno: "))
aluno2 = str(input("Escreva o nome de um aluno: " ))
aluno3 = str(input("Escreva o nome de um aluno: " ))
aluno4 = str(input("Escreva o nome de um aluno: " ))

sorteia = (aluno1, aluno2, aluno3, aluno4)

print(f"Os alunos que estão no sorteio é: {aluno1}, {aluno2}, {aluno3}, {aluno4}")
print("O aluno sorteiado é:" ,random.choice(sorteia))