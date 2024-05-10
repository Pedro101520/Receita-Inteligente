from gemini.response import getRceita
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle

def geraReceita(ingredientes):
    estilo_padrao = ParagraphStyle(
        "padrao",
        fontSize=12,
        textColor='black',
        leading=14,
        spaceAfter=6,
        spaceBefore=6
    )

    texto_receita = getRceita(ingredientes).replace('\n', '<br/>')
    paragrafos = texto_receita.split('<br/>')
    conteudo = []

    for paragrafo in paragrafos:
        conteudo.append(Paragraph(paragrafo, estilo_padrao))

    pdf = SimpleDocTemplate("Receita.pdf", pagesize=letter)
    pdf.build(conteudo)