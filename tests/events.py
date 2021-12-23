import PySimpleGUI as sg

def saludo():
    print('Hola')
    return


layout = [
    [sg.Text('My Layout')],
    [sg.Input],
    [sg.Text('You Entered:'), sg.Text(size=(20,1), key='-OUT-')],
    [sg.Button('OK'), sg.Button('Cancel')],
    [sg.Button('Texto')],
    [sg.Output(size=(20, 10), key='-OUTPUT-')],

]

window = sg.Window('Update Window with input value', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break
    if event == 'Texto':
        pass



window.close()

exit()