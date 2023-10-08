# Desafio: Fazer um tela com o arquivo do aluno.txt
#-PysimpleGUI ou Tkinter

import PySimpleGUI as sg
from random import choice
import Aluno

# Layout
sg.theme("Default1")

layout = [
    [sg.Input(key="nome_aluno", size=(40, 1))],
    [sg.Button("Adicionar"), sg.Button("Remover"), sg.Button("Nome aleatório"), sg.Button("Lista")],
    [sg.Output(key="output", size=(38, 10))]
]

# Janela
window = sg.Window("Lista de alunos", layout)
lista = []

# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == "Lista":
        with open("aulas/aula_16/aluno.txt", "r") as file:
            leitura_texto = file.read()
            name = leitura_texto.split("\n")
        window["output"].update("\n".join(name))

    if eventos == "Nome aleatório":
        Aluno.nome_random(name, window["output"])

    if eventos == "Adicionar":
        request = valores["nome_aluno"]
        if request:
            Aluno.adicionar_aluno(lista, request, window["output"])

    if eventos == "Remover":
        removerrrr = valores["nome_aluno"]
        if removerrrr in name:
            Aluno.remover(name, removerrrr, window["output"])

window.close()



    


