import pandas as pd

df = pd.read_csv('salarios.csv')


print(df)

print("-----HEAD-----")
print(df.head())                                     #ele tras os primeiros itens!

print("-----INFO-----")
print(df.info())                                     #informações do df

print("-----DESCRIBE-----")
print(df.describe())                                 #estatisticas

print("-----FILTROS-----")                           #dois filtros
print(df[(df['Idade'] >20) & (df['Salario'] > 6000 )])
#---------- CLASSIFICAR AS PESSOAS PELA IDADE ----(FunçÃO lambda)
print("------Classificador--------")
df['Classificacao'] = df['Idade'].apply(
    lambda idade: 'Maior de idade' if idade >= 18 else 'Menor de idade'
)
print(df[['Nome','Idade','Classificacao']])

# Usando LAMBDA com for=========================================
print("-----LAMBDA DO FOR-----")
notas = [4,5,7,2,9]
df2 = pd.DataFrame({'Notas': notas})
df2['Resultado'] = df2['Notas'].apply(
    lambda nota: 'Aprovado' if nota >=7 else 'Reprovado'
)

print("-----Salarios do maior para o menor-----")
print(df.sort_values(by='Salario', ascending = False))

#----- ACESSAR LINHAS ESPECIFICAS----
print('Primeiro funcionário')
print(df.iloc[0])
print('Primeiros 3 funcionarios')
print(df.iloc[:3])

print("-----Calculos-----")
print(df['Salario'].count())
print(df['Idade'].mean())
print(df['Salario'].sum())
# ====== min and max .... tambem tem.............

#formas de salvarr
# cria o novo
df.to_csv('salarios_atualizados.csv', index=False)



