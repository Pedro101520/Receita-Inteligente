from gemini.response import exibeReceita

from tkinter import *

def windowReceita(ingredientes):
    receita = exibeReceita(ingredientes)

    app = Tk()
    app.title("Criação de Conta")
    app.geometry("350x500")
    app.configure(background='#ffffff')

    text_box = Text(
        app,
        background="#ffffff",
        foreground="#000",
        wrap=WORD
    )
    text_box.insert(INSERT, receita)
    text_box.place(x=10, y=10, width=330, height=480)

    app.mainloop() 