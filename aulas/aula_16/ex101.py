# Seletor de aluno 
# 1) Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt
# 2) Permita que o porgrama adicione um aluno a lista
# 3) Permita que o programa remova um aluno a lista

import random

def selecionar_aluno():
    with open("aluno.txt", "r") as file:
        aleatorio = file.readlines()
        print(random.choice(aleatorio).strip())

def adicionar_aluno():
    novo_aluno = input("Digite o nome de um aluno: ")
    with open("aluno.txt", "a") as file:
        file.write("\n"+novo_aluno.strip())

def remover_aluno():
    with open("aluno.txt", "r") as file:
        texto = file.read()
        palavra = texto.split("\n")
        
    remover = int(input("Digite o numero para remover o aluno: "))
    del palavra[remover]

   


remover_aluno()