import PySimpleGUI as sg
import pyperclip


layout = [
    [sg.Button('Boton 1')],
    [sg.Button('Boton 2')],
    [sg.Button('Boton 3')],
    [sg.Output(size=(20, 10), key='-OUTPUT-')],
]

window = sg.Window('Título', layout)
eventos = ['Boton 1', 'Boton 2', 'Boton 3']
while True:
    event, values = window.read()
    if event is None:
        break
    if event in eventos:
        print(f"se ha copiado {event}")
        pyperclip.copy(event)


window.close()