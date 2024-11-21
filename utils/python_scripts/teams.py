import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\..\DB_Teste.csv'), sep=';')
df['team_id'] = df['Equipe'].str.extract('(\d+)').astype(int)
teams_df = pd.DataFrame(df[['team_id', 'Equipe']]).drop_duplicates().sort_values(by='team_id', ascending=True).reset_index(drop=True)
teams_df.rename(columns={'Equipe': 'name', 'team_id': 'id'}, inplace=True)
teams_csv = teams_df.to_csv(os.path.join(os.path.dirname(__file__), '..\csv_files\\teams.csv'), sep=';', index=False)
