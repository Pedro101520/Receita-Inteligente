from .informaIngrediente import windowIA

from tkinter import *
import tkinter as tk

def voltar(app):
    app.destroy()
    window()

def window():
    app = Tk()
    app.title("Receitas Inteligentes")
    app.geometry("350x500")

    backgroung = PhotoImage(file="D:/Biblioteca/Documents/Culinaria com IA/assets/img/cozinha.png")
    background_label = Label(app, image=backgroung)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    azul_pastel = "#a8d0e6"
    estilo_botao = {'bg': azul_pastel, 'fg': 'black', 'font': ('Arial', 12, 'bold'), 'width': 10, 'height': 2}
    botaoReceita = tk.Button(app, text="Sugerir Receita", command=lambda: windowIA(app))
    botaoReceita.configure(**estilo_botao)
    botaoReceita.place(x=115, y=370, width=120, height=40)

    botaoDuvida = tk.Button(app, text="Duvida", command=lambda: windowIA())
    botaoDuvida.configure(**estilo_botao)
    botaoDuvida.place(x=115, y=420, width=120, height=40)

    # Button(app, text="Sugerir receita", command=lambda: windowIA()).place(x=120, y=270, width=100, height=20)
    # Button(app, text="Duvidas", command=lambda: windowIA()).place(x=200, y=270, width=100, height=20)

    app.mainloop()