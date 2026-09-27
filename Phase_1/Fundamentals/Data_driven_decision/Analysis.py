import pandas as pd
import matplotlib.pyplot as plt

print("O programa começou!")

# Carregar dataset
df_seguro = pd.read_csv(
    'Autoseg2020A/arq_casco_comp.csv',
    sep=';'
)

print("Dataset carregado!")

# Converter colunas com vírgula decimal
colunas_numericas = ['EXPOSICAO1', 'PREMIO1', 'IS_MEDIA']

for coluna in colunas_numericas:
    df_seguro[coluna] = (
        df_seguro[coluna]
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

#print("Primeiras 10 linhas:")
#print(df_seguro.head(10))

#print("Últimas 10 linhas:")
#print(df_seguro.tail(10))

#print("Tamanho do banco de dados:", df_seguro.shape)

#print("Quantidade de dados nulos:")
#print(df_seguro.isnull().sum().sum())

#print(df_seguro.info())

df_seguro['INDENIZACOES'] = (
    df_seguro['INDENIZ1'] 
)

#print("Primeiras 10 linhas:")
#print(df_seguro.head(10))

# quero retirar o sexo J
df_seguro_plot = df_seguro

# Preparar os dados para o plot
indenizacoes_por_sexo= df_seguro_plot[['SEXO', 'INDENIZACOES']].groupby('SEXO').sum().reset_index()

# Converter para bilhões
indenizacoes_por_sexo['INDENIZACOES_BILHOES'] = (
    indenizacoes_por_sexo['INDENIZACOES'] / 1_000_000_000
)

plt.bar(
    indenizacoes_por_sexo['SEXO'],
    indenizacoes_por_sexo['INDENIZACOES_BILHOES']
)

plt.xlabel('Sexo')
plt.ylabel('Indenizações (R$ bilhões)')
plt.title('TOTAL DE INDENIZAÇÕES POR SEXO')

plt.show()