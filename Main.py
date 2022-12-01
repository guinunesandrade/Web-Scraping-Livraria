from Rascunho import *
from datetime import datetime
from time import sleep
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


def getinfo(url):
    global quantidade_de_livros

    # Ignorando erros de certificado SSL (caso houvesse)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Abrindo a url com BeautifulSoup
    html = urlopen(url, context=ctx).read()
    bs = BeautifulSoup(html, "html.parser")

    # Criando lista de todos os livros numa única página usando a sintaxe BeautifulSoup
    books_list = bs.find_all('li', {'class': "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    # print(books_list)

    # Iterando sobre a lista de livros para obter todas as informações relevantes usando a sintaxe BeautifulSoup
    info_each_book = []
    for book in books_list:
        name = book.find('h3').find('a')['title']
        raw_price = book.find('div', {'class': 'product_price'}).find('p', {'class': 'price_color'}).text
        price = float(raw_price.replace('£', ''))
        stars = book.find('p')['class'][1]
        stock = book.find('p', {'class': 'instock availability'}).text.strip()

        # Acessando cada livro e pegando a sua categoria
        link = 'http://books.toscrape.com/catalogue/' + book.find('h3').find('a')['href']
        url = str(link)
        html = urlopen(url, context=ctx).read()
        bs = BeautifulSoup(html, "html.parser")
        category = bs.find('ul', {'class': "breadcrumb"}).find_all('a')[2].text

        day = datetime.now().strftime('%Y/%m/%d')
        info = [name, price, stars, stock, category, day]
        info_each_book.append(info)
    quantidade_de_livros = len(info_each_book)
    return info_each_book


all_books = []
for i in range(1, 200):
    try:
        info_each_page = getinfo('http://books.toscrape.com/catalogue/page-' + str(i) + '.html')
        all_books += info_each_page
        print(green_text(f'{quantidade_de_livros} livros da Página {i} adicionados...'))
        sleep(0.5)
    except:
        print(yellow_text(f'Total de livros adicionados: {len(all_books)}\n'
                          f'Total de páginas extraídas: {i - 1} '))
        break
# print(all_books)
print(blue_text('Web scraping finalizado!\n'))

# Criando DataFrame a partir dos dados coletados
new = pd.DataFrame(data=all_books, index=range(1, len(all_books) + 1),
                   columns=['Book', 'Price', 'Stars', 'Stock', 'Category', 'Day'])

# Substituindo os dados antigos pelos novos no arquivo csv
new = new.to_csv(r"books_full_data.csv", index=False)
final = pd.read_csv(r"books_full_data.csv")

# Conectando-se ao arquivo csv e preenchendo o banco de dados no servidor sql com esses dados
conn = sqlite3.connect('BOOKS.db')
final.to_sql('Books', conn, index=False, if_exists='replace')
cur = conn.cursor()

# Atualizando a coluna "Stars" com números
cur.execute(''' UPDATE Books SET Stars = 1 WHERE Stars = 'One'; ''')
cur.execute(''' UPDATE Books SET Stars = 2 WHERE Stars = 'Two'; ''')
cur.execute(''' UPDATE Books SET Stars = 3 WHERE Stars = 'Three'; ''')
cur.execute(''' UPDATE Books SET Stars = 4 WHERE Stars = 'Four'; ''')
cur.execute(''' UPDATE Books SET Stars = 5 WHERE Stars = 'Five'; ''')

# Alterando o tipo de dados da coluna "Stars" para INT, para poder manipular melhor esses dados
cur.execute('''ALTER TABLE Books RENAME TO Books_old;''')
cur.execute('''CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY AUTOINCREMENT, Book text NOT NULL, 
Price Real NOT NULL, Stars INT, Stock TEXT, Category TEXT, Day TEXT);''')
cur.execute('''INSERT INTO Books (Book, Price, Stars, Stock, Category, Day) 
SELECT Book, Price, Stars, Stock, Category, Day
FROM Books_old;''')
cur.execute('''DROP TABLE Books_old''')
conn.commit()
conn.close()

# Abrindo uma nova conexão com o banco de dados para criar uma VIEW para análise dos dados
creating_views()

# Criando gráficos e tabelas
chart_cats()

# Criando gráficos e tabelas
chart_livros()

# Criando gráficos e tabelas
chart_n_livros_por_categoria()

# Abrindo a planilha final e encerrando o programa
open_sheets()
