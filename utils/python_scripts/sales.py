import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\..\DB_Teste.csv'), sep=';')

df['client_id'] = df['Cliente'].str.extract('(\d+)').astype(int)
df['vendedor_id'] = df['Vendedor'].str.extract('(\d+)').astype(int)
df['Valor'] = df['Valor'].str.replace('.', '').str.replace(',', '.').str.replace('R$', '').astype(float)

df = df.drop(columns=['Cliente', 'Vendedor'])

df = df[['client_id', 'ID', 'Tipo', 'Data da Venda', 'Categoria', 'vendedor_id', 'Regional', 'Duração do Contrato (Meses)', 'Equipe', 'Valor']]

sales_csv = df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\sales.csv'), sep=';', index=False)