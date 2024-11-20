import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\..\DB_Teste.csv'), sep=';')
df['client_id'] = df['Cliente'].str.extract('(\d+)').astype(int)
clients_df = pd.DataFrame(df[['client_id', 'Cliente']]).drop_duplicates().sort_values(by='client_id', ascending=True).reset_index(drop=True)
clients_df.rename(columns={'Cliente': 'client', 'client_id': 'id'}, inplace=True)
clients_csv = clients_df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\clients.csv'), sep=';', index=False)

# clients = df['Cliente'].unique()
# client_ids = []
# for client in clients:
#     id_through_regex = client.split(' ')[1]
#     client_ids.append(int(id_through_regex))
# clients_dict = {'id': client_ids, 'client': clients}
# clients_df = pd.DataFrame(clients_dict).sort_values(by='id', ascending=True).reset_index(drop=True)

# clients_csv = clients_df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\clients.csv'), sep=';', index=False)