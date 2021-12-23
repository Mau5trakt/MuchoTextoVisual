import pyperclip


def textos(event):
    if event == "A":
        texto = "La letra A"
        return texto
    elif event == "B":
        texto = "La letra B"
        return texto
    elif event == "C":
        texto = "La letra C"
        return texto


def main():
    pyperclip.copy(textos("B"))


if __name__ == "__main__":
    main()