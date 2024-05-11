from .informaIngrediente import windowIA

from tkinter import *
import tkinter as tk

def voltar(app):
    app.destroy()
    window()

def sair(app):
    app.destroy()

def window():
    app = Tk()
    app.title("Receitas Inteligentes")
    app.geometry("350x500")

    backgroung = PhotoImage(file="assets/img/cozinha.png")
    background_label = Label(app, image=backgroung)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    azul_pastel = "#a8d0e6"
    estilo_botao = {'bg': azul_pastel, 'fg': 'black', 'font': ('Arial', 12, 'bold'), 'width': 10, 'height': 2}
    botaoReceita = tk.Button(app, text="Sugerir Receita", command=lambda: windowIA(app))
    botaoReceita.configure(**estilo_botao)
    botaoReceita.place(x=115, y=370, width=120, height=40)

    botaoSair = tk.Button(app, text="Sair", command=lambda: sair(app))
    botaoSair.configure(**estilo_botao)
    botaoSair.place(x=115, y=420, width=120, height=40)

    app.mainloop()