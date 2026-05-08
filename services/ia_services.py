from groq import Groq


class IAService:

    MODELO = "llama-3.3-70b-versatile"

    MAX_TOKENS = 1024

    def __init__(self):
        
        self.cliente = Groq()

    def enviar_mensagem(self, historico: list, system_prompt) str
        
        try:
            
            mensagens = [{"role": "system", "content": system_prompt}] + historico

            resposta = self.cliente.chat.completions.create(
                model=self.MODELO,
                max_tokens=self.MAX_TOKENS
                messages=mensagens,
            )

            return resposta.choices[0].message.cotent
        
        except Exception as e:
            mensagem = str(e)
            if"401" in mensagem or "invalid_api_key" in mensagem.lower():
                raise Exception(" Erro de autenticação: verifique sua GROQ_API")