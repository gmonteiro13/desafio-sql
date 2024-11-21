import pandas as pd
import os
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

df = pd.read_csv('DB_Teste.csv', sep=';')
df['Valor'] = df['Valor'].str.replace('.', '').str.replace(',', '.').str.replace('R$', '').astype(float)

biggest_sale = df['Valor'].max()
smallest_sale = df['Valor'].min()
client_with_biggest_sale = df[df['Valor'] == biggest_sale]['Cliente'].values[0]
client_with_smallest_sale = df[df['Valor'] == smallest_sale]['Cliente'].values[0]
sales_grouped_by_type = df.groupby('Tipo')['Valor'].mean()
number_of_sales_per_client = df['Cliente'].value_counts()

auxiliary_table = df.groupby('Vendedor')['Valor'].sum().sort_values(ascending=False)
csv = auxiliary_table.to_csv('sales_summary.csv', sep=';', index=True)

print(f'O maior valor de venda é {locale.currency(biggest_sale)} e o cliente responsável por essa venda foi o {client_with_biggest_sale}')
print(f'O menor valor de venda é {locale.currency(smallest_sale)} e o cliente responsável por essa venda foi o {client_with_smallest_sale}')
print(f'O número de vendas por cliente é:')
for client, value in number_of_sales_per_client.items():
    print(f"{client}: {value}")
print(f'O valor médio de vendas por tipo é:')
for sale_type, value in sales_grouped_by_type.items():
    print(f"{sale_type}: {locale.currency(value)}")