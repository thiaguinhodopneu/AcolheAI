from groq import Groq


class IAService:

    MODELO = "llama-3.3-70b-versatile"

    MAX_TOKENS = 1024

    def __init__(self):
        
        self.cliente = Groq()

    def enviar_mensagem(self, historico: list, system_prompt)