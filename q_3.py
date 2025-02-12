import re

import pandas as pd
import requests
from db_config import engine

def formatar_data(_data):
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\.\d{3}Z", _data)
    if match:
        return f"{match.group(3)}/{match.group(2)}/{match.group(1)} {match.group(4)}:{match.group(5)}"
    return _data



# 1. Consumir a API e armazenar os dados em um DataFrame
url = "https://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print("Erro ao consumir a API.")
    exit()

# # Tratar os dados
df['created_at'] = df['created_at'].apply(formatar_data)
df['updated_at'] = df['updated_at'].apply(formatar_data)
df = df.drop(columns=['product_colors'])


# 3.1 Armazenar os dados na tabela tb_produto
df.to_sql('tb_produto', engine, if_exists='replace', index=False)
print("Dados armazenados na tabela tb_produto.")

# 3.2 Consumir os dados do PostgreSQL e carregá-los em um DataFrame
query = "SELECT * FROM tb_produto;"
df_from_db = pd.read_sql(query, engine)
print("Dados carregados do PostgreSQL:")
print(df_from_db.head())