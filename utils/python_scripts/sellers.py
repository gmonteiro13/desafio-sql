import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\..\DB_Teste.csv'), sep=';')
df['seller_id'] = df['Vendedor'].str.extract('(\d+)').astype(int)
clients_df = pd.DataFrame(df[['seller_id', 'Vendedor']]).drop_duplicates().sort_values(by='seller_id', ascending=True).reset_index(drop=True)
clients_df.rename(columns={'Vendedor': 'name', 'seller_id': 'id'}, inplace=True)
clients_csv = clients_df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\sellers.csv'), sep=';', index=False)
