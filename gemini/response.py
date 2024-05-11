from geracaoPDF.receita import geraReceita
from calculoCalorias.calorias import windowKcal
from tkinter import messagebox

import google.generativeai as genai

global receita, calorias
calorias = ""
receita = ""

def googleIA(ingredientes):
    global receita, calorias

    GOOGLE_API_KEY="Coloque sua API KEY aqui"
    genai.configure(api_key=GOOGLE_API_KEY)
    generation_config = {
        "candidate_count": 1,
        "temperature": 0.5,
    }

    model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)
    chat = model.start_chat(history=[])

    objetivo = "Aja como um chef super renomado, que é conhecido por dar ideias brilhantes de receitas com ingredientes que são passados para você. Sempre passe o texto no formato de receita e no fim sempre dê a dica do chef. Obrigatoriamente, se te passarem algo não comestivel, você deve informar que não vai escrever a receita."
    prompt = f"{objetivo}{ingredientes}" 
    response = chat.send_message("Limite a sua resposta para no máximo de 200 palavras")
    response = chat.send_message(prompt)
    receita = response.text

    objetivoKcal = "Aja como o melhor nutricionista do mundo. E todas as vezes que alguém te passa uma receita, você consegue passar a quantidade de calorias. Seja objetivo nas respostas e dê algumas dicas sobre a receita."
    promptKcal = f"{objetivoKcal}{receita}" 
    responseKcal = chat.send_message(promptKcal)
    calorias = responseKcal.text

def getReceita():
    global receita
    if receita != "":
        geraReceita(receita)
    else:
        messagebox.showinfo("Aviso", "Para gerar um PDF, primeiro você deve gerar uma receita")  

def getCalorias():
    global calorias
    if calorias != "":
        windowKcal(calorias)
    else:
        messagebox.showinfo("Aviso", "Para saber as calorias, primeiro você deve gerar uma receita")  

def exibeReceita(ingredientes):
    global receita
    googleIA(ingredientes)
    return receita
    