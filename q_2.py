import pandas as pd
import requests
import json
import re
import matplotlib.pyplot as plt


url = "https://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print("Erro ao consumir a API.")
    exit()


# 2.1 Filtrar apenas os produtos com a categoria lipstick
df_lipstick = df[df['category'] == 'lipstick']

# 2.2 Listar as categorias exclusivas presentes no DataFrame
categorias_unicas = df['category'].unique()
print("Categorias únicas:", categorias_unicas)

# 2.3 Criar uma função chamada buscar_produtos
def buscar_produtos(_df, categoria):
    return _df[_df['category'] == categoria]

# Utilizar a função para a categoria 'pencil'
df_pencil = buscar_produtos(df, 'pencil')
print("Produtos da categoria 'pencil':")
print(df_pencil[['brand', 'name', 'price']].iloc[:10])

# 2.4 Utilizar expressão regular para transformar o campo "created_at"
def formatar_data(_data):
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\.\d{3}Z", _data)
    if match:
        return f"{match.group(3)}/{match.group(2)}/{match.group(1)} {match.group(4)}:{match.group(5)}"
    return _data

df['created_at'] = df['created_at'].apply(formatar_data)
print(df["created_at"].iloc[:10])

# 2.5 Exportar o DataFrame filtrado (lipstick) para o formato .json
df_lipstick.to_json('lipstick_products.json', orient='records', lines=True)

# 2.6 Criar um gráfico de barras das 10 marcas com mais produtos do tipo lipstick
top_marcas= df_lipstick['brand'].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
top_marcas.plot(kind='bar', color='skyblue')
plt.title('Top 10 Marcas com Mais Produtos de Lipstick')
plt.xlabel('Marca')
plt.ylabel('Número de Produtos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()