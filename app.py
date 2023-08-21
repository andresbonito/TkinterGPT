import os
import chatgpt
import tela
from dotenv import load_dotenv
load_dotenv()

# p2go = os.getenv('OPENAI_API_KEY_p2go')
# bossini = os.getenv('OPENAI_API_KEY_bossini')
gmail = os.getenv('OPENAI_API_KEY_99gmail')

def criar_pergunta(assunto, tipo, dificuldade, pergunta_exemplo):
    return chatgpt.criar_pergunta(gmail, assunto, tipo, dificuldade, pergunta_exemplo)

def responder_pergunta(pergunta_a_ser_respondida):
    return chatgpt.responder_pergunta(gmail, pergunta_a_ser_respondida)

tela.criar_tela(criar_pergunta, responder_pergunta)
