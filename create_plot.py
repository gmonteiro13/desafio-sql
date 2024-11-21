import sqlite3
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os_path = os.path.dirname(__file__)
conn = sqlite3.connect(os.path.join(os_path, 'dev.db'))
query = os.path.dirname(__file__) + '\queries\quarterly_sales.sql'

df = pd.read_sql_query(open(query).read(), conn)
conn.close()

sns.set_theme(style="whitegrid")
ax = sns.barplot(x='year_quarter', y='sales_values', data=df)
plt.title('Vendas por trimestre')
plt.ylabel('Valor das vendas (BRL)')
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: "R$ {:,}".format(int(x)).replace(",", ".")))
plt.xlabel('Trimestre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(os_path, 'images\quarterly_sales.png'))
plt.show()