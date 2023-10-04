# Seletor de aluno 
# 1) Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt
# 2) Permita que o porgrama adicione um aluno a lista
# 3) Permita que o programa remova um aluno a lista

import random

def mostrando_a_lista():
    with open("aluno.txt","r") as file:
        print("-"*30)
        print(f"Abrindo o arquivo:\n{file.read()}")

def selecionar_aluno():
    with open("aluno.txt", "r") as file:
        aleatorio = file.readlines()
        print("-"*30)
        print(f"O aluno selecionado é: {random.choice(aleatorio)}".strip())

def adicionar_aluno():
    print("-"*30)
    novo_aluno = input("Digite o nome de um aluno: ")
    with open("aluno.txt", "a") as file:
        file.write("\n"+novo_aluno.strip())
    
    print("-"*30)
    file_atualizada = open("aluno.txt","r")
    print(f"Lista atualizada:\n{file_atualizada.read()}")

def remover_aluno():
    with open("aluno.txt", "r") as file:
        texto = file.read()
        palavra = texto.split("\n")
        
    print("-"*30)
    remover = int(input("Digite o numero para remover o aluno: "))
    del palavra[remover]

    print("-"*30)
    print(f"Lista atualizada:\n{palavra}")

mostrando_a_lista()
selecionar_aluno()
adicionar_aluno()
remover_aluno()