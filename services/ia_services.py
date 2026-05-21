from groq import Groq
import os


class IAService:

    MODELO = "llama-3.3-70b-versatile"

    MAX_TOKENS = 1024

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        self.cliente = Groq(
            api_key=api_key
        )

    def enviar_mensagem(self, historico: list, system_prompt: str) -> str:

        try:

            mensagens = [
                {
                    "role": "system",
                    "content": system_prompt
                }
            ] + historico

            resposta = self.cliente.chat.completions.create(
                model=self.MODELO,
                max_tokens=self.MAX_TOKENS,
                messages=mensagens
            )

            conteudo = resposta.choices[0].message.content

            return conteudo

        except Exception as e:

            mensagem = str(e)

            if "401" in mensagem or "invalid_api_key" in mensagem.lower():

                raise Exception(
                    "Erro de autenticação: verifique sua GROQ_API_KEY."
                )

            elif "429" in mensagem or "rate_limit" in mensagem.lower():

                raise Exception(
                    "Limite de requisições atingido. Aguarde um momento."
                )

            else:

                raise Exception(
                    f"Erro na API da Groq: {mensagem}"
                )


if __name__ == "__main__":

    servico = IAService()

    historico_teste = [
        {
            "role": "user",
            "content": "Olá! Estou me sentindo ansioso."
        }
    ]

    system_teste = "Você é um chatbot acolhedor."

    resposta = servico.enviar_mensagem(
        historico_teste,
        system_teste
    )

    print("\nResposta da IA:")
    print(resposta)