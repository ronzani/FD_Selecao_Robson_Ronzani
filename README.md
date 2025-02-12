# Teste FD

Este repositório contém a solução do teste, organizada em arquivos conforme o número de cada questão.  

Além das respostas às questões, o projeto inclui:  
1. Uma **API FastAPI** que fornece dados de produtos.  
2. Uma **aplicação Streamlit** que consome a API e exibe os dados em uma interface web.  

## 📌 Como executar o projeto  

### Instalando dependências
1. No terminal, execute:  
   ```bash
   pip install -r requirements.txt
   ```

### 🚀 Executando a API (FastAPI)  
1. No terminal, execute:  
   ```bash
   uvicorn main:app --reload
   ```
2. A API estará disponível em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

### 🌐 Executando a aplicação Web (Streamlit)  
1. No terminal, execute:  
   ```bash
   streamlit run q_05.py
   ```
2. A aplicação estará disponível em: [http://localhost:8501](http://localhost:8501)  

---

