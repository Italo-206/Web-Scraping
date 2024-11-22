import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Função para corrigir a URL se necessário
def verificar_e_corrigir_url(url):
    if not url.startswith(("http://", "https://")):
        url_corrigida = f"https://{url}"
    else:
        url_corrigida = url

    # Perguntar ao usuário se deseja usar a URL corrigida
    if url != url_corrigida:
        usar_corrigida = messagebox.askyesno(
            "URL Corrigida",
            f"A URL fornecida parece estar incompleta.\nVocê quis dizer: {url_corrigida}?\nDeseja continuar com essa URL?"
        )
        if not usar_corrigida:
            return None
    return url_corrigida

# Função principal para realizar o scraping
def realizar_scraping():
    url = entry_url.get()  # Pega a URL inserida pelo usuário
    
    if not url:  # Verifica se a URL está vazia
        messagebox.showerror("Erro", "Por favor, cole uma URL válida.")
        return
    
    url = verificar_e_corrigir_url(url)
    if not url:  # Se o usuário cancelar a URL sugerida
        return

    try:
        # Faz a requisição HTTP para o site
        response = requests.get(url)
        response.raise_for_status()
        
        # Faz o parsing do conteúdo HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar todos os links <a> com texto
        links = soup.find_all('a', href=True)
        textos = [link.get_text(strip=True) for link in links if link.get_text(strip=True)]
        
        if not textos:
            messagebox.showerror("Erro", "Nenhum texto foi encontrado na página.")
            return
        
        # Salvar em arquivo CSV
        df = pd.DataFrame(textos, columns=["Texto"])
        df.to_csv('dados_extraidos.csv', index=False)
        
        messagebox.showinfo("Sucesso", "Scraping concluído! Dados salvos em 'dados_extraidos.csv'.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao site: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Web Scraping")

# Interface gráfica
label = tk.Label(root, text="Cole a URL do site desejado aqui:")
label.pack(pady=5)

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

botao = tk.Button(root, text="Iniciar Scraping", command=realizar_scraping)
botao.pack(pady=10)

root.mainloop()
