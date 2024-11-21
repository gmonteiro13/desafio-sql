import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\..\DB_Teste.csv'), sep=';')
df['team_id'] = df['Equipe'].str.extract('(\d+)').astype(int)
df['seller_id'] = df['Vendedor'].str.extract('(\d+)').astype(int)
sellers_teams_df = pd.DataFrame(df[['seller_id', 'team_id']]).drop_duplicates().sort_values(by='seller_id', ascending=True).reset_index(drop=True)
sellers_teams_df.rename(columns={'seller_id': 'seller_id', 'team_id': 'team_id'}, inplace=True)
sellers_teams_csv = sellers_teams_df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\sellers_teams.csv'), sep=';', index=False)