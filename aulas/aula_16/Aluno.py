from random import choice

def words_random(list,saida):
    saida["b"].update("\n",choice(list))

def adicionar_aluno(lista,insert,saida):
    lista.append(insert)
    file=open("List_Student/alunos.txt","a")
    file.write("\n"+ insert)
    saida["b"].update("\n".join(lista))
  
def remover(lista,delete_name,saida):
    lista.remove(delete_name)
    with open("List_Student/alunos.txt","w") as file:
        file.write("")
    saida["b"].update("\n".join(lista))
