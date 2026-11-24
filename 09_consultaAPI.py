import json, requests

nome = input("Digite seu nome!:")

localidade = 0
while localidade < 1 or localidade > 2:
    localidade = int(input("Você deseja selecionar uma localidade? \n [1] sim \n [2] não \n"))
    estados = '''
    Qual o estado que deseja buscar?
    [33] - RJ
    [35] - SP
    [31] - MG
    [53] - DF
    [43] - RS
 '''   
if localidade == 1 : #Sim, quero localidadae
    uf = input(estados)
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={uf}')
    
if localidade == 2 : #Não, quero todos os territórios do Brasil        

    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
    
print(''']
      Escolha o período de tempo:
      
      [1] - 1930 -
      [2] - 1930 - 1940
      [3] - 1940 - 1950
      [4] - 1950 - 1960
      [5] - 1960 - 1970
      [6] - 1970 - 1980
      [7] - 1980 -1990
      [8] - 1990 - 2000
      [9] - 2000 - 2010
      ''') 

tempo = int(input('Selecione o período desejado:')) - 1
dados_json = json.loads(resultado.text)
print(dados_json[0]['res'][tempo])