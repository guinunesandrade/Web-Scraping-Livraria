import sqlite3
import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

conn = sqlite3.connect('BOOKS.db')
cur = conn.cursor()
cur.execute('DROP VIEW IF EXISTS Prices;')
cur.execute('''CREATE VIEW Prices AS
SELECT Category, round(avg(Price), 2) AS "Average Price", 
round(avg(Stars), 1) AS "Average Stars"
FROM Books
GROUP BY Category
ORDER BY 3 DESC, 2;''')
cur.execute('DROP VIEW IF EXISTS livros_por_categoria;')
cur.execute('''CREATE VIEW livros_por_categoria AS
SELECT Category, count(id) AS "Nº de livros"
FROM Books
GROUP BY Category
ORDER BY 2 DESC, 1;''')
conn.commit()
conn.close()

# Nova conexão com o banco de dados para adicionar a "VIEW" para fazer um gráfico no excel.
conn = sqlite3.connect('BOOKS.db')
cur = conn.cursor()
cur.execute("SELECT * FROM PRICES")
data = cur.fetchall()

# Criando a planilha para montar a tabela que eservirá de base para o gráfico
wb = Workbook()
ws_table = wb.create_sheet(title='Categorias')

# Adicionando os nomes das colunas à planilha da tabela
ws_table.append(('Categorias', 'Preço', 'Estrelas'))
print(data)

# Adicionando os dados armazenados no banco de dados à planilha da tabela
for row in data:
    ws_table.append(row)

# Criando o objeto gráfico do tipo barra em colunas
chart1 = BarChart()
chart1.type = "col"

# Nomeando os eixos x e y
chart1.y_axis.title = 'Preços/Recomendações'
chart1.x_axis.title = 'Categorias'

# Escolhendo o estilo de cores (estilo 12 recomendado na própria documentação)
chart1.style = 12

# Adicionando as categorias ("cats") e os dados referentes a cada uma ("data") da tabela ao gráfico
data = Reference(ws_table, min_col=2, min_row=1, max_row=len(data) + 1, max_col=3)
cats = Reference(ws_table, min_col=1, min_row=2, max_row=len(data) + 1)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)

# Posição da legenda no gráfico ("r" de "right", isto é, à direita do gráfico)
chart1.legend.position = "r"

# Altura e largura
chart1.height = 12
chart1.width = 35

# Criando a planilha do gráfico e adicionando o gráfico montado a ela
ws_chart = wb.create_sheet(title='graph categorias')
ws_chart.add_chart(chart1, "A1")

# Removendo a planilha vazia padrão inerente à criação do arquivo xlsx
standard_sheet = wb['Sheet']
wb.remove(standard_sheet)

# Salvando as planilhas no formato xlsx (Excel)
wb.save("bar.xlsx")

