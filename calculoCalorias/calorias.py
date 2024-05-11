from tkinter import *

def windowKcal(kcal):
    app = Tk()
    app.title("Informações Nutricionais")
    app.geometry("350x500")
    app.configure(background='#ffffff')

    text_box = Text(
        app,
        background="#ffffff",
        foreground="#000",
        wrap=WORD
    )
    text_box.insert(INSERT, kcal)
    text_box.place(x=10, y=10, width=330, height=480)

    app.mainloop() 