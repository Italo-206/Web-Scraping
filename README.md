Projeto de Web Scraping: Coleta de Dados de Sites com Interface Gráfica
Este projeto demonstra como realizar a coleta de dados de um site utilizando Web Scraping com uma interface gráfica criada em Tkinter. O objetivo é extrair os textos de links disponíveis em uma página da web e armazená-los em um arquivo CSV de forma organizada. Utiliza as bibliotecas BeautifulSoup para o parsing do HTML, requests para requisições e pandas para manipulação e armazenamento dos dados.

Descrição
O projeto realiza os seguintes passos:

Entrada de URL: O usuário insere a URL desejada através de uma interface gráfica.

Coleta de Dados: O programa realiza uma requisição HTTP para obter o HTML do site.

Extração de Links: Utilizamos BeautifulSoup para extrair os textos de todos os links disponíveis na página.

Armazenamento dos Dados: Os textos extraídos são organizados em um arquivo CSV chamado dados_extraidos.csv.

Este projeto é um exemplo simples e didático de como coletar dados de sites que não oferecem uma API, utilizando o método de web scraping.

Tecnologias Usadas
Python: Linguagem de programação utilizada para implementar a lógica do web scraping.
Tkinter: Biblioteca para criação da interface gráfica.
Requests: Biblioteca para realizar requisições HTTP e obter o conteúdo das páginas.
BeautifulSoup: Biblioteca para fazer o parsing do conteúdo HTML e extrair dados.
Pandas: Biblioteca para salvar os dados extraídos em um arquivo CSV.
Funcionalidades
Interface gráfica para facilitar o uso por iniciantes.
Coleta textos de links de um site qualquer.
Trata exceções como falhas nas requisições ou ausência de links na página.
Salva os textos extraídos em um arquivo CSV para uso posterior.
Observações Importantes
Estrutura do Site: Este projeto busca links genéricos no HTML da página. Ele pode não funcionar corretamente caso o site utilize estruturas específicas ou carregue conteúdo dinamicamente.

Conteúdo Dinâmico: Alguns sites, como aqueles que utilizam JavaScript para carregar dados, podem exigir ferramentas como Selenium para extração adequada.

Exemplo de Teste: Um bom site para testar o código é o Globo.com, que possui várias seções com links estáticos no HTML.

Como Rodar o Projeto
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/web-scraping-project.git
cd web-scraping-project
Instale as dependências: Certifique-se de ter Python instalado. Execute:

bash
Copiar código
pip install requests beautifulsoup4 pandas
Execute o programa:

bash
Copiar código
python seu_script.py
Cole a URL do site: Insira a URL desejada na interface gráfica e clique em "Iniciar Scraping".

Resultados:

Os textos dos links serão extraídos e salvos no arquivo dados_extraidos.csv.
Estrutura do Arquivo CSV
O arquivo dados_extraidos.csv conterá uma única coluna chamada Texto, com os textos dos links extraídos da página.

Texto
Link 1: Texto aqui
Link 2: Texto aqui
...
Melhorias Futuras
Adicionar suporte a sites dinâmicos usando Selenium.
Permitir a escolha do nome e local do arquivo CSV.
Implementar suporte para paginação em sites com múltiplas páginas de conteúdo.
