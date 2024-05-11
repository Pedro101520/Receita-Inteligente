from gemini.response import getReceita, getCalorias
from geracaoPDF.exibereceita import windowReceita

from tkinter import *
import tkinter as tk
from tkinter import messagebox

def windowIA(appOpcoes):
    from .opcoes import voltar
    
    appOpcoes.destroy()

    app = Tk()
    app.title("Receitas Inteligentes")
    app.geometry("350x500")

    backgroung = PhotoImage(file="assets/img/Input.png")
    background_label = Label(app, image=backgroung)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    txtIng=Text(app, bg="#add8e6")
    txtIng.place(x=83, y=200, width=185, height=180)

    azul_pastel = "#a8d0e6"
    estilo_botao = {'bg': azul_pastel, 'fg': 'black', 'font': ('Arial', 12, 'bold'), 'width': 10, 'height': 2}
    
    def validaIngredientes():
        ingredientes = txtIng.get("1.0", "end").strip()
        if not ingredientes:
            messagebox.showinfo("Aviso", "Por favor, informe os ingredientes")  
        else:
            windowReceita(ingredientes)

    botaoReceita = tk.Button(app, text="Gerar Receita", command=lambda: validaIngredientes())
    botaoReceita.configure(**estilo_botao)
    botaoReceita.place(x=42, y=400, width=120, height=40)

    botaoPDF = tk.Button(app, text="PDF", command=lambda: getReceita())
    botaoPDF.configure(**estilo_botao)
    botaoPDF.place(x=42, y=450, width=120, height=40)
    
    botaoCalorias = tk.Button(app, text="Calorias", command=lambda: getCalorias())
    botaoCalorias.configure(**estilo_botao)
    botaoCalorias.place(x=185, y=400, width=120, height=40)

    botaoSair = tk.Button(app, text="Voltar", command=lambda: voltar(app))
    botaoSair.configure(**estilo_botao)
    botaoSair.place(x=185, y=450, width=120, height=40)

    app.mainloop()