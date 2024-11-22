# Projeto de Web Scraping com Interface Gráfica: Coleta de Dados de Sites

Este projeto demonstra como realizar a coleta de dados de um site utilizando **Web Scraping** com uma interface gráfica simples. O objetivo é extrair os textos de links presentes em uma página da web e armazená-los em um arquivo CSV organizado. O projeto utiliza as bibliotecas **BeautifulSoup** para o parsing do HTML, **requests** para a requisição da página, e **Tkinter** para criar a interface gráfica.

---

## Descrição

O projeto realiza os seguintes passos:

1. **Entrada de URL**: O usuário insere a URL do site através da interface gráfica.
   
2. **Coleta de Dados**: A página HTML é carregada usando a biblioteca **requests**.

3. **Análise do Conteúdo HTML**: Utilizamos **BeautifulSoup** para extrair os textos dos links.

4. **Armazenamento dos Dados**: Os textos extraídos são salvos em um arquivo CSV chamado `dados_extraidos.csv`.

Este projeto é um exemplo simples e didático de como coletar dados de sites que não oferecem uma API, utilizando o método de web scraping.

---

## Tecnologias Usadas

- **Python**: Linguagem de programação utilizada para implementar o projeto.
- **Tkinter**: Biblioteca para criar a interface gráfica.
- **Requests**: Biblioteca para realizar requisições HTTP e obter o conteúdo das páginas.
- **BeautifulSoup**: Biblioteca para fazer o parsing do conteúdo HTML e extrair dados.
- **Pandas**: Biblioteca para armazenar os dados extraídos em um arquivo CSV.

---

## Funcionalidades

- **Interface gráfica** para facilitar o uso por iniciantes.
- Coleta textos de links de qualquer página HTML estática.
- Trata exceções, como falhas na requisição ou ausência de links na página.
- Salva os textos extraídos em um arquivo CSV para uso posterior.

---

## Observações Importantes

- **Estrutura do Site**: Este projeto busca links genéricos no HTML da página. Ele pode não funcionar corretamente caso o site utilize estruturas específicas ou carregue conteúdo dinamicamente.

- **Conteúdo Dinâmico**: Alguns sites, como aqueles que utilizam **JavaScript** para carregar dados, podem exigir ferramentas como **Selenium**.

- **Exemplo de Teste**: Um bom site para testar o código é o [Globo.com](https://www.globo.com), que possui várias seções com links estáticos no HTML.

---

## Como Rodar o Projeto

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/web-scraping-project.git
   cd web-scraping-project
