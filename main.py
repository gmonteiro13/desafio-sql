import pandas as pd

df = pd.read_csv('DB_Teste.csv', sep=';')

df['Valor'] = df['Valor'].str.replace('.', '').str.replace(',', '.').str.replace('R$', '').astype(float)

auxiliary_table = df.groupby('Vendedor')['Valor'].sum().reset_index()

csv_file = auxiliary_table.to_csv('auxiliary_table2.csv', index=False)