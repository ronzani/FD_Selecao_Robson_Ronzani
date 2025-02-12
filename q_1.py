import pandas as pd
from matplotlib import pyplot as plt


url = "https://raw.githubusercontent.com/datasets/finance-vix/main/data/vix-daily.csv"
df = pd.read_csv(url) # ler csv

df_linhas = df.iloc[:6] # listar 6 primeiras linhas
# print(df_linhas)

# print(df.info()) # lista info dataset

# print(df.describe()) # Lista as estatísticas básicas do dataframe.


df = df.dropna(axis=1, how='any') # Remover linhas com valor nulo

df["DATE"] = pd.to_datetime(df["DATE"]) # Converte a coluna DATE para detetime

df['Volatility Range'] = df['HIGH'] - df['LOW']

# Cria uma coluna Ano_Mes
df['ANO_MES'] = df['DATE'].dt.to_period('M')

# Agrupa por 'ANO_MES' e calcula a média da coluna 'CLOSE'
df_media_close = df.groupby('ANO_MES')['CLOSE'].mean().reset_index()

df_media_close = df_media_close.sort_values('ANO_MES') # Ordena por 'ANO_MES'

print(df_media_close.head())
# print(df_media_close.info())


# Criar o gráfico
plt.figure(figsize=(12, 6))  # Define o tamanho do gráfico
plt.plot(df_media_close['Ano_Mes'], df_media_close['CLOSE'], marker='o', linestyle='-', color='b')

# Adicionar título e rótulos aos eixos
plt.title('Média Mensal do VIX (CLOSE)', fontsize=16)
plt.xlabel('Ano/Mês', fontsize=12)
plt.ylabel('Média do VIX (CLOSE)', fontsize=12)

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Adicionar grade para facilitar a leitura
plt.grid(True)

# Exibir o gráfico
plt.tight_layout()  # Ajusta o layout para evitar cortes nos rótulos
plt.show()
