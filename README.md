<h1 align="center"> Livraria </h1>

<h2 align="center"> Web Scraping de uma livraria fictícia e análise dos dados utilizando Python e SQL </h2>

<h3> :arrow_forward: Status do Projeto: </h3> :white_check_mark: Concluído :white_check_mark: 

<h3> :hammer: Tecnologias do Projeto: </h3>

- `Python`
- `SQL`
- `CSV`

<h3>:warning: Ferramentas Necessárias: </h3>

- `SQLite`
- `IDE qualquer (Pycharm, Atom, VS Code, etc)`

<h3>:books: Bibliotecas utilizadas: </h3>

- `datetime`
- `time`
- `sqlite3`
- `pandas`
- `urllib.request`
- `bs4`
- `ssl`
<p align="justify"> Nota: Certifique-se de ter todas elas vinculadas à sua IDE. </p>

<h3>:clipboard: Descrição do Projeto: </h3>

<p align="justify">
Nesse projeto realizou-se um web scraping de uma livraria fictícia com o objetivo de extrair as informações dos livros contidas no site, tais como nome do livro, preço, nível de recomendação dos usuários (de 1 a 5 estrelas), disponibilidade no estoque, categoria e data da extração (caso houvesse atualização periódica das informações). Com essas informações, criou-se um dataframe para visualização inicial dos dados, os quais foram posteriormente salvos em um arquivo csv, para, finalmente, tratá-los em um banco de dados. Utilizando comandos SQL, foi possível agrupar em uma "VIEW" as informações dos livros por categoria e ordená-las pelo nível de recomendação dos usuários (em ordem decrescente) e preço (em ordem crescente), como mostrado na figura 1.
</p>

<img src="Categorias mais bem avaliadas.png">

<p align="center">
Figura 1: Categorias mais bem avaliadas
</p>

<p align="justify">
A figura 2 contém o código SQL utilizado para a criação da VIEW "Prices" mostrada na figura 1.
</p>

<img src="Código da View Prices.png">

<p align="center">
Figura 2: Código SQL da VIEW "Prices"
</p>


<p align="justify">
A figura 3 contém as informações principais de todos os livros do site.
</p>

<img src="Info da junção de todos os livros.png">

<p align="center">
Figura 3: Informações principais de todos os livros. 
</p>

<p align="justify">
Com as informações contidas nas figuras 1, 2 e 3, pode-se dizer que a média de recomendação de todos livros do site é baixa, tendo em vista uma avaliação de 2.9 estrelas. Emboras algumas categorias, tais como "Adult Fiction", "Erotica", "Novels" e "Christian Fiction", contenham poucos livros (apenas 9, representando menos de 1% do total de livros), elas possuem uma média de avaliação acima de 4 estrelas, com as duas primeiras contendo livros com preço de quase metade da média de preço de todos os livros (média de preço total igual 35.07, como mostrado na figura 3), sendo estas duas boas escolhas de recomendação para usuários que não queiram gastar muito dinheiro mas que desejam ler livros bem avaliados. 
<br>
Em contrapartida, categorias como "Psychology", "Short Stories", "Cultural", além de possuirem livros com as piores avaliações (menor que 2 estrelas), estes são caros comparados com a média de preço de todos os livros, portanto, tais categorias e seus respectivos livros, deveriam ser os menos recomendados para os usuários de modo geral, até para aqueles que se interessem por esses assuntos, isto é, deveria-se investir na inclusão de livros mais interessentes e baratos nessas categorias, a fim de recomendá-las para os usuários que se interessem na leitura de livros desses assuntos.
<br>
Com a visualização desses dados, por fim, é possível concluir que, de modo geral, os livros presentes no site são caros e com uma média relativamente baixa de avaliação, e, que comparados aos melhores livros das melhores categorias (os quais reprsentam menos de 1% do total), deve-se adotar uma política de exclusão dos livros que sejam extremamente caros e mal avaliados (como mostrado na figura 1) e inclusão de mais livros com a qualidade e preço dos mais bem avaliados para que a quantidade destes suba de 1% para pelo menos metade do total (a depender das metas da livraria) e o site possa ser melhor recomendado entre os usuários e atraente nas campanhas de marketing.
</p>
