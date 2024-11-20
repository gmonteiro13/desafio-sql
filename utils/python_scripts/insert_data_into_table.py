import os
import pandas as pd
import sqlite3

os_path = os.path.dirname(__file__)
sales_csv = os.path.join(os_path, '..\csv_files\sales.csv')
clients_csv = os.path.join(os_path, '..\csv_files\clients.csv')
sellers_csv = os.path.join(os_path, '..\csv_files\sellers.csv')

def insert_data_into_table(csv_file, table_name):
    df = pd.read_csv(csv_file, sep=';')
    df.columns = df.columns.str.strip()
    conn = sqlite3.connect(os.path.join(os_path, '..\..\dev.db'))
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

insert_data_into_table(clients_csv, 'clients')
insert_data_into_table(sellers_csv, 'sellers')
insert_data_into_table(sales_csv, 'sales')