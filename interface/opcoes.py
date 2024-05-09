from .informaIngrediente import windowIA

from tkinter import *

def window():
    app = Tk()
    app.title("Receitas Inteligentes")
    app.geometry("350x500")

    filename = PhotoImage(file="D:/Biblioteca/Documents/Culinaria com IA/assets/img/cozinha.png")
    background_label = Label(app, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    app.configure(background='#dde')
    Label(
        app,
        text = "Quantidade de noticias - Entre 1 a 10:",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtQtde=Entry(app)
    txtQtde.place(x=225, y=10, width=50, height=20)

    Button(app, text="Sugerir receita", command=lambda: windowIA()).place(x=120, y=270, width=100, height=20)
    Button(app, text="Duvidas", command=lambda: windowIA()).place(x=200, y=270, width=100, height=20)

    

    app.mainloop()