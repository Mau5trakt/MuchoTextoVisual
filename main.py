import PySimpleGUI as sg
import pyperclip
import webbrowser

def textos(event):
    if event == "Saludo":
        texto = 'Saludos 👋\n' \
                'Somos Express Global Import\n' \
                '*Agencia de envíos de Miami a Nicaragua totalmente fuera de aduana*\n\n' \
                'Ofrecemos dos servicios: Marítimo y aéreo.\n\n' \
                'Tiempos de Despachos:\n\n' \
                'Vía aérea: 1 vez por semana martes y jueves. Con entrega en 3 días hábiles a partir de la fecha de salida. Desde $9 la libra.  \n\n' \
                'Vía marítima: 1 vez por semana los días martes Con entrega en 15 - 20 días hábiles a partir de la fecha de salida del contenedor de Miami a Nicaragua. Desde $3 la libra.  Con un mínimo de 10 libras y opción de consolidado gratis. \n\n' \
                'Electrónicos de alto valor, Maquinaria industria les, vehículos, cargas especiales o de  gran volumen son sujetos a cotización para tarifas especiales libre de aduana.\n'
        return texto
    elif event == "Indicaciones":
        texto = 'Al momento  de hacer tu compra en línea o enviar tu carga a nuestras bodegas debes poner tu nombre y a la par de tu nombre ExpressGlobal/Maritimo-Aereo (depende del servicio que quiera)\n' \
                'Ejemplo:\n' \
                'Juan Pérez/ExpressGlobal/Marítimo\n\n' \
                'ESTA ESPECIFICACIÓN ES MUY IMPORTANTE PARA PODER DIFERENCIAR TU CARGA Y ENVIARLA CORRECTAMENTE.\n\n' \
                '📍Dirección en Miami:\n' \
                '8548 NW 72 ST. Miami,FL 33166.\n\n' \
                'Tarifas Totalmente fuera de aduana.\n' \
                'Retiras en nuestras oficinas en Managua.\n\n' \
                '📍Dirección en Nicaragua: De donde fue la Vicky 2c. Abajo, 1c. Al lago, frente a ENACAL. Plaza San Mateo, Managua.'
        return texto
    elif event == "Tmiami":
        texto = 'Oficina Miami: 786-614-2889 (WhatsApp)'
        return texto
    elif event == "Dnic":
        texto = "📍Dirección en Nicaragua: Los Robles, del hotel Colón 2 cuadras y media al sur, casa #46"
        return texto
    elif event == "Dmiami":
        texto = "📍Dirección en Miami:\n"\
                "8548 NW 72 ST. Miami,FL 33166.\n\n"\
                "Tarifas Totalmente fuera de aduana. "
        return texto
    elif event == "Cuenta":
        texto = 'Número de cuenta:\n'\
                'VALERIA SOLIS SOZA\n\n'\
                '358576973\n\n'\
                'BAC Dólares'
        return texto
    elif event == "Consulta":
        texto =  'Podria indicarme el tracking number por favor?'
        return texto
    elif event == "Espera":
        texto = 'Un momento por favor se esta haciendo la consulta en el sistema. '
        return texto
    elif event == "Despedida":
        texto =  "Es un placer atenderle, gracias por Elegir Express Global Import  para enviar sus paquetes, buen día. "
        return texto
    elif event == "Retiro":
        texto = "Hola, de parte de Express Global Import le informamos que tiene entrega a su nombre, puede pasar a retirar en horario de oficina, buen día  ☺️☺️"
        return texto
    elif event == "Transporte":
        texto = "Hola, de momento estamos teniendo un retraso con muestro transportista que nos hace llegar la carga a nuestras oficinas, en cuanto tengamos su carga le estaremos avisando, buen día."
        return texto
    elif event == "Clasificación":
        texto ="Hola, estamos clasificando los paquetes recibidos en cuanto tengamos todos los paquetes clasificados te estaremos avisando para que vengas por el tuyo. "
        return texto


def ventana():
    global layout_column
    sg.theme('DarkAmber')
    layout_column = [
        [sg.Text('Mucho Texto Visual', justification='center')],
        [sg.Button('Saludo', size=(20, 1))],
        [sg.Button('Indicaciones', size=(20, 1))],
        [sg.Button('Tmiami', size=(20, 1))],
        [sg.Button('Dnic', size=(20, 1))],
        [sg.Button('Dmiami', size=(20, 1))],
        [sg.Button('Cuenta', size=(20, 1))],
        [sg.Button('Consulta', size=(20, 1))],
        [sg.Button('Espera', size=(20, 1))],
        [sg.Button('Despedida', size=(20, 1))],
        [sg.Button('Retiro', size=(20, 1))],
        [sg.Button('Transporte', size=(20, 1))],
        [sg.Button('Clasificación', size=(20, 1))],
        [sg.Output(size=(20, 10), key='-OUTPUT-')],
        [sg.Text('github.com/Mau5trakt'), sg.Button('go', size=(1, 1))]
    ]

    layout = [[sg.Column(layout_column, element_justification='center')]]

    window = sg.Window('Mucho Texto Visual', layout, )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        lista = ["Saludo","Indicaciones","Tmiami", "Dnic", "Dmiami", "Cuenta", "Consulta", "Espera", "Despedida", "Retiro", "Transporte", "Clasificación"]
        if event in lista:
            print(f"Se ha copiado {event}")
            pyperclip.copy(textos(event))
        elif event == 'go':
            webbrowser.open('https://github.com/Mau5trakt')

    window.close()


def main():
    ventana()

if __name__ == "__main__":
    main()
