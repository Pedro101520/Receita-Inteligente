from tkinter import *
import tkinter as tk

def windowIA(appOpcoes):
    from .opcoes import voltar
    
    appOpcoes.destroy()

    app = Tk()
    app.title("Receitas Inteligentes")
    app.geometry("350x500")
    app.configure(background='#dde')

    backgroung = PhotoImage(file="D:/Biblioteca/Documents/Culinaria com IA/assets/img/Input.png")
    background_label = Label(app, image=backgroung)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    txtIng=Text(app, bg="#add8e6")
    txtIng.place(x=83, y=220, width=185, height=180)

    azul_pastel = "#a8d0e6"
    estilo_botao = {'bg': azul_pastel, 'fg': 'black', 'font': ('Arial', 12, 'bold'), 'width': 10, 'height': 2}
    botaoCalorias = tk.Button(app, text="Calorias", command=lambda: windowIA(app))
    botaoCalorias.configure(**estilo_botao)
    botaoCalorias.place(x=17, y=450, width=100, height=40)

    botaoReceita = tk.Button(app, text="Gerar Receita", command=lambda: windowIA())
    botaoReceita.configure(**estilo_botao)
    botaoReceita.place(x=122, y=450, width=120, height=40)

    botaoSair = tk.Button(app, text="Voltar", command=lambda: voltar(app))
    botaoSair.configure(**estilo_botao)
    botaoSair.place(x=247, y=450, width=80, height=40)

    app.mainloop()