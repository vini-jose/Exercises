import random

def nome_random(lista, saida):
    saida.update("\n" + random.choice(lista))

def adicionar_aluno(lista, insert, saida):
    lista.append(insert)
    with open("aulas/aula_16/aluno.txt", "a") as file:
        file.write("\n" + insert)
    saida.update("\n".join(lista))

def remover(lista, delete_name, saida):
    lista.remove(delete_name)
    with open("aulas/aula_16/aluno.txt", "w") as file:
        file.write("\n".join(lista))
    saida.update("\n".join(lista))
