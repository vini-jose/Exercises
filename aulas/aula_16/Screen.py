# Desafio: Fazer um tela com o arquivo do aluno.txt
#-PysimpleGUI ou Tkinter

import PySimpleGUI as sg
import Aluno
import random 

# Layout
sg.theme("Reddit")

layout = [[sg.Input(key="nome_aluno", size=(40, 1))],
          [sg.Button("Adicionar"), sg.Button("Remover"), sg.Button("Nome aleatório"), sg.Button("Lista")],
          [sg.Output(key="output",size=(38,10))]
        ]

#Janela
window = sg.Window("Lista de aluno", layout)
lista = []


#Ler ps eventos
while True:
    eventos,valores=window.read()
    if eventos == sg.WIN_CLOSED:
        window.close()
        break

    if eventos == "Lista":
        list_student=open("aluno.txt")
        leitura_texto=list_student.read()
        name = list(map(str,leitura_texto.split("\n")))
        window["output"].update("\n".join(name))

    if eventos == "Nome aleatorio":
        window["output"].update((random.choice(name)))
        
    if eventos == "Adicionar":
        request = valores["nome_aluno"]
        if request:
            Aluno.adicionar_aluno(lista,request,window)
    
    if eventos == "Remover":
        removerrrr = valores["nome_aluno"]
        if request in name:
            Aluno.remover(name,removerrrr,window)



    


