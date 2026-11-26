import requests
import pandas as pd
import random
import sqlite3
import datetime
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0 Safari/537.36'}
baseURL = "https://books.toscrape.com/catalogue/page-"

livros = []

dataHoje = datetime.date.today().strftime("%d-%m-%Y")
agora = datetime.datetime.now()

paginaLimite = 3
cardTempMin = 1
cardTempMax= 3
pagTempMin = 2
pagTempMax = 4

bancoDeDados = "banco_filmes.db"

saidaCSV = "livros_{}.csv"

# ==============================================================================
#COLETA DE DADOS
#===============================================================================

for pagina in range(1, paginaLimite + 1):
    url = f"{baseURL}{pagina}.html"
    print(f"Coletando dados da pagina {pagina}:{url}")
    resposta = requests.get(url, headers=headers,timeout=30)
    resposta.raise_for_status()                        
    soup = BeautifulSoup(resposta.text, "html.parser")
    cards= soup.find_all("article", class_="product_pod")
#que sono    
    if not cards:
        print("NENHUM LIVRO ENCONTRAAADO")
        break
    
    for card in cards :
        try:
            titulo_tag = card.find("h3").find("a")
            preco_tag = card.find("p", class_="price_color")
            estoque_tag = card.find("p", class_="instock")
            
            titulo  = titulo_tag.get("title", "N/A")
            preco   = preco_tag.get_text(strip=True)
            estoque = estoque_tag.get_text(strip=True)
            
            if titulo !="N/A" :
                livros.append({
                    "Titulo" : titulo,
                    "Preco"  : preco,
                    "estoque": estoque
                })
                
                print(f"Livro: {titulo}")
                print(f"Preco:{preco}")
                print(f"estoque:{estoque}")
                print(f"-" * 30)
            tempo = random.uniform(cardTempMin, cardTempMax) 
            time.sleep(tempo)   
        except Exception as errinho:
            print(f"Erro ao processar o cartão: {errinho}")
    tempo = random.uniform(pagTempMin, pagTempMax)         
    time.sleep(tempo) 
     
#=======================================================================================
#DATAFRAME E CSV
#=======================================================================================

df = pd.DataFrame(livros) 

print(df.head())  

df.to_csv(
    saidaCSV,
    index=False,
    encoding="utf-8-sig",
    quotechar = "'",
    quoting = 1
) 

#===============================================================================================
#bando de dadososososoososoosososossosooosspssospsppspsp Squlite
#=============================================================================================

conn = sqlite3.connect(bancoDeDados)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT,
        Preco TEXT,
        Estoque TEXT 
    )          
''')

for livro in livros :
    try:
        cursor.execute('''
            INSERT INTO livros (Titulo, Preco, Estoque)               
            VALUES (?,?,?)
        ''',    (
                livro['Titulo'],
                livro['Preco'],
                livro['Estoque']
                )
        
        ) 
    except Exception as e:
        print(f"Erro {e} ao inserir o livro{livro['Titulo']}")
conn.commit()
conn.close()                                   
              


print('-' * 30)
print('Dados coletados e salvos com sucesso')
print(f'Total de livros: {len(livros)}')
print(f'Arquivos salvo em: {saidaCSV}')
print(f'Inicio: {agora.strftime('%H:%M:%S')}')
print(f'fim: {fim.strftime('%H:%M:%S')}')
print('-' * 30)