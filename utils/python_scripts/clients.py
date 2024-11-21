import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\..\DB_Teste.csv'), sep=';')
df['client_id'] = df['Cliente'].str.extract('(\d+)').astype(int)
clients_df = pd.DataFrame(df[['client_id', 'Cliente']]).drop_duplicates().sort_values(by='client_id', ascending=True).reset_index(drop=True)
clients_df.rename(columns={'Cliente': 'name', 'client_id': 'id'}, inplace=True)
clients_csv = clients_df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\clients.csv'), sep=';', index=False)