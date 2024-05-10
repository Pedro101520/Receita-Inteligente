import google.generativeai as genai

from tkinter import messagebox

global receita
receita = """"""

def googleIA(ingredientes):
    global receita

    GOOGLE_API_KEY="API Key"
    genai.configure(api_key=GOOGLE_API_KEY)
    generation_config = {
        "candidate_count": 1,
        "temperature": 0,
    }
    safety_settings = {
        "HARASSMENT": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE",
    }
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)
    chat = model.start_chat(history=[])

    objetivo = "Aja como um chef super renomado, que é conhecido por dar ideias brilhantes de receitas com ingredientes que são passados para você. Sempre passe o texto no formato de receita e no fim sempre dê a dica do chef. Obrigatoriamente, se te passarem algo não comestivel, você deve informar que não vai escrever a receita."
    prompt = f"{objetivo}{ingredientes}" 

    response = chat.send_message("Limite a sua resposta para no máximo de 200 palavras")
    response = chat.send_message(prompt)
    receita = response.text
    messagebox.showinfo("Aviso", "PDF Gerado") 
    # print(response.text)
    print(receita)

def getRceita(ingredientes):
    global receita
    googleIA(ingredientes)
    return receita