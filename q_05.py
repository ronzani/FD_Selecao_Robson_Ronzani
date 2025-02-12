import streamlit as st
import requests


st.title("Produtos")

# URL da API FastAPI
API_URL = "http://localhost:8000//api/v1/produtos"

# Função para buscar os dados da API
def buscar_dados():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Erro ao buscar dados: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Erro ao conectar à API: {e}")
        return []


dados = buscar_dados()

# Exibir os dados em uma tabela
if dados:
    st.write("### Lista de Produtos")
    st.dataframe(dados)  # Exibe os dados em uma tabela
else:
    st.write("Nenhum dado encontrado.")