# Desafio Triggo

## Descrição
O desafio consiste em criar um programa que leia um arquivo CSV e realize as seguintes tarefas em Python:
- Construir uma tabela auxiliar que sumarize o valor vendido por cada vendedor, ordenando do maior para o menor;
- Imprimir e identificar qual foi o cliente responsável pela venda com maior valor e com menor valor;
- Imprimir valor médio por Tipo de venda;
- Imprimir o número de vendas realizada por cliente.

Além disso, é necessário construir queries SQL que identifiquem os seguintes cenários:
- Construir o modelo de relacionamento com as categorias utilizadas em todos os campos do arquivo CSV;
- Listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020;
- Listar a equipe de cada vendedor;
- Construir uma tabela que avalia trimestralmente o resultado de vendas e plote um gráfico deste histórico.

## Requisitos
- Python
- SQLite

## Antes da execução
- Crie um ambiente virtual para instalar as dependências do projeto:
```bash
python -m venv venv
```

- Ative o ambiente virtual:
```bash
source venv/bin/activate
```

- Instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

Instale a extensão [SQLite](vscode:extension/alexcvzz.vscode-sqlite) no VSCode para executar/visualizar o banco de dados.
Recarregue a janela do VSCode após a instalação da extensão pelo comando `Ctrl+Shift+P` e digitando `Reload Window`.

## Execução
- Para executar a primeira parte do desafio, basta rodar o script `python_tasks.py`:
```bash
python python_tasks.py
```
Além dos outputs requeridos pelo desafio, o script também gera um arquivo `sales_summary.csv` com a tabela auxiliar.

- Para executar a segunda parte do desafio, crie o banco de dados `dev.db` na pasta raiz do projeto e execute o script schema.sql:
```bash
sqlite3 dev.db < schema.sql
```

ou, no VSCode, execute o comando `SQLite: Open Database` e selecione o arquivo `dev.db`. Em seguida, execute o comando `SQLite: Run Query` e selecione o arquivo `schema.sql`.

- Rode o script `utils/python_scripts/insert_data_into_table.py` para inserir os dados de todos os arquivos csv em `csv_files` no banco de dados:
```bash
python utils/python_scripts/insert_data_into_table.py
```

- Execute as queries SQL na pasta `queries` para visualizar os resultados.
- Execute o script python `create_plot.py` para gerar o gráfico trimestral de vendas:
```bash
python create_plot.py
```
Uma imagem será criada no diretório `images`.