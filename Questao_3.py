import time
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = pd.DataFrame(dados_extraidos)
print("1")
print(df)

df = df.dropna(subset=['id_processo'])
print(" ")
print("2")
print(df)

df['status'] = df['status'].str.capitalize()
print(" ")
print("3")
print(df)

df['valor_causa'] = df['valor_causa'].str.replace('R$', '').str.strip()
df['valor_causa'] = df['valor_causa'].str.replace('.', '')

df['valor_causa'] = df['valor_causa'].str.replace(',', '.')

df['valor_causa'] = pd.to_numeric(df['valor_causa'])

print(" ")
print("4")
print(df)

