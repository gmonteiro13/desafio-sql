import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../../DB_Teste.csv'), sep=';')

df['client_id'] = df['Cliente'].str.extract('(\d+)').astype(int)
df['seller_id'] = df['Vendedor'].str.extract('(\d+)').astype(int)
df['team_id'] = df['Equipe'].str.extract('(\d+)').astype(int)
df['Data da Venda'] = pd.to_datetime(df['Data da Venda'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
df['Valor'] = df['Valor'].str.replace('.', '').str.replace(',', '.').str.replace('R$', '').astype(float)

df = df.drop(columns=['Cliente', 'Vendedor', 'Equipe'])

df = df[['client_id', 'ID', 'Tipo', 'Data da Venda', 'Categoria', 'seller_id','Duração do Contrato (Meses)', 'team_id', 'Valor']]
df.rename(columns={'ID': 'contract_id', 'Tipo': 'type', 'Data da Venda': 'sale_date', 'Categoria': 'category',
                   'Regional': 'region', 'Duração do Contrato (Meses)': 'contract_duration', 'Valor': 'value'}, inplace=True)

sales_csv = df.to_csv(os.path.join(os.path.dirname(__file__), '../csv_files/sales.csv'), sep=';', index=False)