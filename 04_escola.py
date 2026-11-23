# ! = Diferennte
# == Igual
# > Maior
# < Menor
# >= Maior ou igual
# <= Menor ou igual

mediaAluno = int(input(" Qual a média do aluno: \nR: "))
tipoEscola = input("Qual o tipo do colégio : \n [1] Público \n [2]Particular \nR:")
freqAluno = int(input(" Qual a frequencia do aluno: \nR: "))
mediaCorte = 7
freqCorte = 70

if tipoEscola == "2" :
    if mediaAluno >= mediaCorte and freqAluno >= freqCorte:
        print("aprovado!:3")  
    else:
        print("Reprovado :(")
        
if tipoEscola == "1":
    if mediaAluno >= mediaCorte or freqAluno >= freqCorte:
        print("aprovado! :3")
    else:
        print("Reprovado :(")
                
                        

