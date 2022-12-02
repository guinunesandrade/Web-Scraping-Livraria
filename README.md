<h1 align="center"> Livraria </h1>

<h2 align="center"> Automatização de ETL de uma livraria fictícia e análise dos dados utilizando Python, SQL e Excel </h2>

<h3> :arrow_forward: Status do Projeto: </h3> :white_check_mark: Concluído :white_check_mark: 

<h3> :hammer: Tecnologias do Projeto: </h3>

- `Python`
- `SQL`
- `CSV`
- `Excel`

<h3>:warning: Ferramentas Necessárias: </h3>

- `SQLite`
- `IDE qualquer (Pycharm, Atom, VS Code, etc)`
- `Microsoft Excel`

<h3>:books: Bibliotecas utilizadas: </h3>

- `datetime`
- `time`
- `sqlite3`
- `pandas`
- `urllib.request`
- `bs4`
- `ssl`
- `openpyxl`
- `os`

<p align="justify"> Nota: Certifique-se de ter todas elas vinculadas à sua IDE. </p>

<h3>:clipboard: Descrição do Projeto: </h3>

<p align="justify">
Nesse projeto realizou-se uma automatização completa de extração (web scraping dos dados de livros de uma livraria), tratamento (usando Python e SQL) e análise dos dados (usando Excel), com o objetivo de extrair as informações dos livros contidas no site, tais como nome do livro, preço, nível de recomendação dos usuários (de 1 a 5 estrelas), disponibilidade no estoque, categoria e data da extração (caso houvesse atualização periódica das informações). Com essas informações, criou-se um dataframe para visualização inicial dos dados, os quais foram posteriormente salvos em um arquivo csv (arquivo de segurança caso algum dado seja perdido posteriormente), para, por fim, salvá-los em um banco de dados. Utilizando comandos SQL em Pyhton por meio da biblioteca sqlite3, foi possível criar "VIEWS", as quais, utilizando a biblioteca "openpyxl", serviram de base para a construção de gráficos no Excel. Todo esse processo, junto aos gráficos representados abaixo, são criados de forma automática ao executar o código em Pyhton. 
<br>
É válido ressaltar que os arquivos "BOOKS.db", "books_full_data.csv" e "livraria.xlsx" disponibilizados no repositório são criados de forma automática ao executar pela primeira vez o código (caso você os queira inicialmente vazios para testar o código) e atualizados toda vez que o mesmo é executado.
</p>
<p align="justify">
A figura 1, por exemplo, representa o gráfico contendo as informações de preço e recomendação de livros por categoria.
</p>

![image](https://user-images.githubusercontent.com/119316984/205152197-33195d4c-1076-4c93-8e39-b7619a740871.png)

<p align="center">
Figura 1: Média de preço e recomendação de livros por categoria
</p>

<p align="justify">
A figura 2 representa o gráfico com as informações de preço e recomendação médios de todos os livros do site
</p>

![image](https://user-images.githubusercontent.com/119316984/205154828-6dfd48cd-e3d6-49bf-9262-2fbc4b28cb60.png)

<p align="center">
Figura 2: Média de preço e recomendação de todos os livros do site
</p>

<p align="justify">
Observando as Figura 1 e 2, pode-se inferir que o nível de recomendação dos livros não possui uma relação proporcional com a média de preços dos livros de cada categoria, ou seja, há categorias com um alto índice de recomendação e livros com preço abaixo da média ("Adult Fiction", "Erotica" e "Christian Fiction"), ao passo que há categorias com um baixo nível de recomendação e livros com preço acima da média (como, por exemplo, "Politics", "Parenting", "Short Stories" e "Cultural").
</p>

<p align="justify">
A figura 3 apresenta a quantidade de livros por categoria.
</p>

![image](https://user-images.githubusercontent.com/119316984/205155988-fb54bd52-695a-44ff-8ec6-5abed50e449b.png)

<p align="center">
Figura 3: Quantidade de livros por categoria. 
</p>

<p align="justify">
Com a figura 3, é possível observar que há poucas categorias com muitos livros (mais de 100) e a maior parte com menos de 20 livros, sendo 10 delas com apenas 1 livro.
<br>
Com as informações contidas nas figuras 1, 2 e 3, pode-se dizer que a média de recomendação de todos livros do site é baixa, tendo em vista uma avaliação de 2.9 estrelas. Emboras algumas categorias, tais como "Adult Fiction", "Erotica", "Novels" e "Christian Fiction", contenham poucos livros (apenas 9, representando menos de 1% do total de livros), elas possuem uma média de avaliação acima de 4 estrelas, com as duas primeiras contendo livros com preço de quase metade da média de preço de todos os livros (média de preço total igual 35.07, como mostrado na figura 3), sendo estas duas boas escolhas de recomendação para usuários que não queiram gastar muito dinheiro mas que desejam ler livros bem avaliados. 
<br>
Em contrapartida, categorias como "Psychology", "Short Stories", "Cultural", além de possuirem livros com as piores avaliações (menor que 2 estrelas), estes são caros comparados com a média de preço de todos os livros, portanto, tais categorias e seus respectivos livros, deveriam ser os menos recomendados para os usuários de modo geral, até para aqueles que se interessem por esses assuntos, isto é, deveria-se investir na inclusão de livros mais interessentes e baratos nessas categorias, a fim de recomendá-las para os usuários que se interessem na leitura de livros desses assuntos.
<br>
Com a visualização desses dados, por fim, é possível concluir que, de modo geral, os livros presentes no site são caros e com uma média relativamente baixa de avaliação, e, que comparados aos melhores livros das melhores categorias (os quais reprsentam menos de 1% do total), deve-se adotar uma política de exclusão dos livros que sejam extremamente caros e mal avaliados (como mostrado na figura 1) e inclusão de mais livros com a qualidade e preço dos mais bem avaliados para que a quantidade destes suba de 1% para pelo menos metade do total (a depender das metas da livraria) e o site possa ser melhor recomendado entre os usuários e atraente nas campanhas de marketing.
</p>
