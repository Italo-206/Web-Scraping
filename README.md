# Projeto de Web Scraping: Coleta de Títulos de Notícias

Este projeto demonstra como realizar a coleta de dados de um site de notícias utilizando **Web Scraping**. O objetivo é extrair os títulos das notícias de uma página da web e armazená-los em um formato estruturado (arquivo CSV). O projeto utiliza as bibliotecas **BeautifulSoup** para fazer o parsing do HTML e **requests** para fazer a requisição da página.

## Descrição

O projeto realiza os seguintes passos:

1. **Coleta de Dados**: A página HTML de um site de notícias é carregada usando a biblioteca **requests**.
   
2. **Análise do Conteúdo HTML**: Utilizamos **BeautifulSoup** para fazer o parsing da página e extrair os títulos das notícias.

3. **Armazenamento dos Dados**: Os títulos das notícias extraídos são salvos em um arquivo CSV, usando **pandas** para uma melhor organização.

Este projeto é um exemplo simples de como coletar dados de um site que não oferece uma API, utilizando o método de web scraping.

## Tecnologias Usadas

- **Python**: Linguagem de programação utilizada para implementar a lógica do web scraping.
- **Requests**: Biblioteca para realizar requisições HTTP e obter o conteúdo das páginas.
- **BeautifulSoup**: Biblioteca para fazer o parsing do conteúdo HTML e extrair dados.
- **Pandas**: Biblioteca para armazenar os dados extraídos em um arquivo CSV de forma estruturada.

## Funcionalidades

- Coleta os títulos de notícias de um site de notícias.
- Trata exceções, como falhas nas requisições ou ausência de elementos na página.
- Salva os dados extraídos em um arquivo CSV para uso posterior.
- Código simples e fácil de entender, ideal para iniciantes em web scraping.

## Observações Importantes

- **Alteração na Estrutura**: O código assume que o site usa a classe `feed-post-link` para os links das notícias, mas isso pode mudar dependendo da estrutura do HTML. Você pode inspecionar o código da página para verificar as classes corretas.
  
- **Conteúdo Dinâmico**: Alguns sites, como o da Globo, carregam conteúdo dinamicamente usando **JavaScript**. Isso pode impedir que o BeautifulSoup extraia dados corretamente, pois ele apenas lê o HTML estático da página. Se esse for o caso, você pode precisar de uma ferramenta como **Selenium** para lidar com JavaScript.

- **Paginação**: Esse código captura as notícias da página inicial, mas o site pode ter várias páginas de notícias. Para lidar com isso, você precisaria adicionar lógica de paginação ao código.

## Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/web-scraping-project.git
