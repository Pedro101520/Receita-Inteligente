from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from tkinter import messagebox
import re

def geraReceita(receita):
    estilo_padrao = ParagraphStyle(
        "padrao",
        fontSize=12,
        textColor='black',
        leading=14,
        spaceAfter=6,
        spaceBefore=6
    )

    texto_receita = receita
    
    texto_receita = re.sub(r'\*(.*?)\*', r'<b>\1</b>', texto_receita)
    texto_receita = texto_receita.replace('\n', '<br/>')
    paragrafos = texto_receita.split('<br/>')

    conteudo = []

    for paragrafo in paragrafos:
        conteudo.append(Paragraph(paragrafo, estilo_padrao))

    pdf = SimpleDocTemplate("Receita.pdf", pagesize=letter)
    messagebox.showinfo("Aviso", "PDF da receita gerado!") 
    pdf.build(conteudo)