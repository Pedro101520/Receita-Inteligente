from gemini.response import googleIA

from tkinter import *

def windowIA():
    app = Tk()
    app.title("Receitas Inteligentes")
    app.geometry("500x300")
    app.configure(background='#dde')
    Label(
        app,
        text = "Informe os ingredientes: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtIng=Entry(app)
    txtIng.place(x=225, y=70, width=150, height=150)

    Button(app, text="Calorias", command=lambda: googleIA(txtIng.get())).place(x=200, y=270, width=100, height=20)
    Button(app, text="Salvar PDF", command=lambda: googleIA(txtIng.get())).place(x=350, y=270, width=100, height=20)
    app.mainloop()