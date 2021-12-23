import PySimpleGUI as sg
import pyperclip

def func(message='Default message'):
    print(message)

layout = [[sg.Button('1', key=lambda: func(pyperclip.copy('ayeye'))),
           sg.Button('2', key=lambda: func(pyperclip.copy('Boton 2'))),
           sg.Button('3'),
           sg.Exit()]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if callable(event):
        event()
    elif event == '3':
        func('Button 3 pressed')

window.close()