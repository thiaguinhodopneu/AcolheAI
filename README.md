# AcolheAI
# AcolheAI 💙

Chatbot de apoio emocional com IA desenvolvido em Python, Flask e integração com a API da [Groq](https://groq.com?utm_source=chatgpt.com) usando o modelo Llama 3.

O projeto foi criado com foco em:

* acolhimento emocional
* conversas mais humanas
* apoio inicial para ansiedade, estresse e sobrecarga emocional
* prática de engenharia de prompt
* integração frontend + backend + IA

---

# 🚀 Tecnologias utilizadas

* Python
* Flask
* Flask-CORS
* HTML
* CSS
* JavaScript
* API da Groq
* Modelo Llama 3

---

# 📁 Estrutura do projeto

```plaintext
AcolheAI/
│
├── core/
│   └── prompt_mestre.py
│
├── services/
│   └── ia_services.py
│
├── frontend/
│   ├── index.html
│   └── style.css
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧠 Como o sistema funciona

O fluxo do chatbot funciona assim:

```plaintext
Usuário → Frontend → Flask → Groq API → Resposta da IA
```

### Explicando:

1. O usuário envia uma mensagem pelo navegador
2. O frontend envia essa mensagem para o Flask
3. O Flask envia o histórico + prompt mestre para a IA
4. A API da Groq gera a resposta
5. O chatbot responde na tela

---

# ⚙️ Como instalar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/AcolheAI.git
```

---

## 2. Entrar na pasta

```bash
cd AcolheAI
```

---

# 🐍 Instalar Python

Baixe o Python:

[Python Oficial](https://www.python.org/downloads/?utm_source=chatgpt.com)

⚠️ Durante a instalação marque:

```plaintext
Add Python to PATH
```

---

# 🔥 Criar ambiente virtual

## Windows

```bash
python -m venv .venv
```

---

# 🔥 Ativar ambiente virtual

## PowerShell

Se aparecer erro de permissão:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

# 📦 Instalar dependências

```bash
pip install flask flask-cors groq python-dotenv
```

---

# 🔑 Configurar API da Groq

Crie uma conta:

[Groq Console](https://console.groq.com/keys?utm_source=chatgpt.com)

---

# Criar variável de ambiente

## PowerShell

```powershell
$env:GROQ_API_KEY="SUA_CHAVE_AQUI"
```

---

# ▶️ Rodar o projeto

```bash
python main.py
```

---

# 🌐 Abrir no navegador

```plaintext
http://localhost:5500
```

---

# 💡 Funcionalidades

* Chat em tempo real
* Integração com IA
* Prompt mestre emocional
* Respostas mais humanas
* Histórico de conversa
* Frontend moderno
* Simulação de digitação
* Apoio emocional inicial

---

# 🧠 Engenharia de Prompt

O projeto utiliza um Prompt Mestre baseado no framework:

```plaintext
P.T.R.F
```

* Persona
* Tarefa
* Restrição
* Formato

Além disso:

* comportamento emocional
* segurança emocional
* acolhimento humanizado
* prevenção de respostas robóticas

---

# 🚨 Aviso importante

O AcolheAI NÃO substitui:

* psicólogos
* psiquiatras
* profissionais da saúde mental

O chatbot oferece apenas:

* apoio emocional inicial
* acolhimento
* conversa segura

Em situações graves procure ajuda profissional.

---

# ☎️ Apoio emocional gratuito no Brasil

## CVV

```plaintext
188
```

Atendimento 24h gratuito.

[CVV Oficial](https://www.cvv.org.br/?utm_source=chatgpt.com)

---

# 🏥 Outras formas de ajuda

* CAPS
* SUS
* Clínicas-escola de faculdades
* Projetos sociais

---

# 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e prática de:

* IA
* Engenharia de Prompt
* Backend
* Frontend
* Integração de APIs
* UX conversacional

---

# ⭐ Objetivo do projeto

Criar um chatbot mais humano, acolhedor e emocionalmente inteligente, evitando respostas genéricas e melhorando a experiência do usuário durante conversas emocionais.
