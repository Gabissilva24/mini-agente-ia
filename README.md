# 🤖 Mini Agente de Planejamento com IA

Um agente inteligente que gera planos de ação personalizados usando o modelo **Llama 3.3 70B** através da API do Groq.

## [🌐 Ver demonstração ao vivo →](https://huggingface.co/spaces/gabisilvaa/mini-agente-ia)


---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte dos meus estudos em Inteligência Artificial e Python. 

### 🎯 O que aprendi construindo isso:

- **APIs de IA**: Como integrar e usar modelos de linguagem (LLMs) em aplicações
- **Interfaces Web**: Transformar código Python em aplicação web usando Gradio
- **Segurança**: Gerenciar credenciais sensíveis com variáveis de ambiente
- **Deploy**: Hospedar aplicações de IA em produção (Hugging Face Spaces)
- **Prompt Engineering**: Como estruturar prompts para obter melhores resultados

### ✨ Funcionalidades:

- Gera planos de ação estruturados usando IA generativa
- Interface web simples e funcional
- Tratamento básico de erros
- Configuração via arquivo `.env`

### 🛠️ Tecnologias Utilizadas:

- **Python 3.8+**
- **Groq API** - Acesso ao modelo Llama 3.3 70B
- **Gradio** - Framework para criar interfaces web
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **Hugging Face Spaces** - Plataforma de deploy

---

## 🚀 Como Executar Localmente

### Pré-requisitos:
- Python 3.8+
- Chave da API Groq (gratuita em [console.groq.com](https://console.groq.com))

### Instalação:
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/mini-agente-ia.git
cd mini-agente-ia

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure a variável de ambiente
echo "GROQ_API_KEY=sua_chave_aqui" > .env

# Execute
python mini_agente.py  # Versão terminal
# ou
python app.py  # Versão web
```

---

## 📁 Estrutura do Projeto
```
agente/
│
├── mini_agente.py      # Versão linha de comando
├── app.py              # Versão web (Gradio)
├── requirements.txt    # Dependências
├── .env.example        # Template de configuração
├── .gitignore          # Arquivos ignorados
└── README.md          # Documentação
```

---

## 🌐 Versão Web no Hugging Face

Gere planos de ação diretamente no navegador, sem precisar instalar nada!

🔗 [Ver demonstração ao vivo →](https://huggingface.co/spaces/gabisilvaa/mini-agente-ia)

### ✨ Como Usar
1. Digite sua tarefa no campo de texto  
2. Clique em **"Gerar Plano"**  
3. Receba um plano personalizado em segundos 🚀  

💡 Exemplos:
- "Criar um aplicativo web de tarefas"
- "Plano de estudos para aprender Python em 3 meses"
- "Organizar viagem para o Japão por 15 dias"

*(Esta versão web utiliza as mesmas tecnologias descritas acima, com deploy feito no Hugging Face Spaces.)*

---

## 🎓 Aprendizados e Desafios

Este foi meu primeiro projeto integrando IA em uma aplicação real. Alguns desafios que enfrentei:

- **Entender APIs**: Aprendi a ler documentação e fazer requisições HTTP
- **Debugging**: Lidar com erros de autenticação e modelos descontinuados
- **Deploy**: Configurar secrets e variáveis de ambiente em produção
- **UX**: Pensar na experiência do usuário ao projetar a interface

**O que melhorou minhas habilidades:**
- Leitura de documentação técnica
- Resolução de problemas práticos
- Entendimento do ecossistema de IA/LLMs

---

## 🔮 Próximos Passos

Ideias que quero implementar:
- [ ] Adicionar histórico de conversas
- [ ] Criar diferentes "personas" de agentes (estudo, viagem, negócios)
- [ ] Exportar planos gerados em PDF
- [ ] Comparar respostas de diferentes modelos

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar como referência!

---

## 👤 Autor

**Gabriele Soares da Silva** 

- GitHub: https://github.com/Gabissilva24/mini-agente-ia

---

*Projeto desenvolvido como parte do meu portfólio de estudos em Inteligência Artificial*