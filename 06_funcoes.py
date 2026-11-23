
def minhaFuncao(curso) :
    print("Curso de " + curso + " na Clarify.")
    
minhaFuncao("Python")
minhaFuncao("Java")
minhaFuncao("Claude")
minhaFuncao("SQL")

cidades = ['São Paulo','Ribeirão Pires','Mauá', 'Cotia', 'Poá']
contador = 0

def minhaFuncaoMelhorada(informacao, X) :
    print(str(X) + ' - ' + informacao)
    

for cidade in cidades :
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)
    
executar = True
while executar :
    nome        = input("Digite seu nome:")
    anoAtual    = int(input("Digite o ano atual:"))
    anoNasc     = int(input("Digite o ano que voce nasceu:"))
    idade = anoAtual - anoNasc
    print("Olá"+ nome + " voce tem " + str(idade) + " anos. ") 
    opcao = input("Voce deseja testar novamente? \n[1] Sim ou [2] Não?")
if opcao == "2" or "Não" or "Não" or "Não" or "Nao" or "nao" :
    executar = False


