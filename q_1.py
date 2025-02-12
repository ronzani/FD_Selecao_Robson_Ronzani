from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt


url = "https://raw.githubusercontent.com/datasets/finance-vix/main/data/vix-daily.csv"
df = pd.read_csv(url) # ler csv

print(df.iloc[:6]) # listar 6 primeiras linhas

print(df.info()) # lista info dataset

print(df.describe()) # Lista as estatísticas básicas do dataframe.

df = df.dropna(axis=1, how='any') # Remover linhas com valor nulo

df["DATE"] = pd.to_datetime(df["DATE"]) # Converte a coluna DATE para detetime

df['Volatility Range'] = df['HIGH'] - df['LOW']

# Cria uma coluna Ano_Mes
df['ANO_MES'] = df['DATE'].dt.to_period('M').astype(str)

# Agrupa por 'ANO_MES' e calcula a média da coluna 'CLOSE'
df_media_close = df.groupby('ANO_MES')['CLOSE'].mean().reset_index()

df_media_close = df_media_close.sort_values('ANO_MES') # Ordena por 'ANO_MES'

# Cria o gráfico
plt.figure(figsize=(12, 6))
plt.plot(df_media_close['ANO_MES'], df_media_close['CLOSE'])

plt.title('Média Mensal (CLOSE)', fontsize=16)
plt.xlabel('Ano/Mês', fontsize=12)
plt.ylabel('Média (CLOSE)', fontsize=12)

# Exibir o gráfico
plt.tight_layout()
plt.show()

# Exportar o data frame
formato_data_horario = datetime.now().strftime('%d%m%y_%H%M')
nome_arquivo = f"finance_{formato_data_horario}.parquet"

# Exporta para o formato .parquet
df_media_close.to_parquet(nome_arquivo, index=False)

