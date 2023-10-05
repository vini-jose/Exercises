# Desafio: Fazer um tela com o arquivo do aluno.txt
#-PysimpleGUI ou Tkinter

import PySimpleGUI as sg

sg.theme("Dark Grey 13")

layout = [[sg.Text("Filename")],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window("Get filename  example", layout)

event, values = window.read()
window.close()