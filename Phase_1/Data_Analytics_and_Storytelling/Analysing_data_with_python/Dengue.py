import pandas as pd
import numpy as np

import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px 

print("O programa começou!")


df_dengue = pd.read_excel('BD_dengue.xlsx')

#print("Excel carregado!")
#print(df_dengue.head())
print(f'Tamanho do banco de dados: {df_dengue.shape}')
#print(df_dengue.dtypes)
print(f'Quantidade de dados nulos: {df_dengue.isnull().sum().sum()}')

#informações sobre a base de dados:

print(df_dengue.info())

#verificar valores unicos
print(df_dengue.nunique())

#precisamos calcular a quantidade de pessoas que pegaram dengue por municipio por ano 

df_dengue ['ano'] = df_dengue['data_infeccoes'].dt.year

#print(df_dengue.head())

infeccoes_municipio = df_dengue.groupby(['ano', 'municipio', 'uf'])['qtd_infeccoes'].sum().reset_index()
#print(infeccoes_municipio.head())

#agrupar por estado e ano (KDD)

infeccoes_estado = df_dengue.groupby(['ano', 'uf'])['qtd_infeccoes'].sum().reset_index()

#print(infeccoes_estado.head())

#ESTATÍSTICA DESCRITIVA

#print(infeccoes_estado.describe())

#interpretação da estatistica descritiva utilizando o grafico de boxplot

#vamos olhar o ano de 2023
infeccoes_estado_2023 = infeccoes_estado[infeccoes_estado['ano'] == 2023]
print(infeccoes_estado_2023)

#criar boxplot comparando a quantidade de infecções por ano 
#plt.figure(figsize=(10,6))
#sns.boxplot(data = infeccoes_estado, x = 'ano', y = 'qtd_infeccoes', hue = 'ano', palette='viridis', legend = False)
#sns.boxplot(data = infeccoes_estado_2023, x='ano', y = 'qtd_infeccoes', hue='ano', palette = 'viridis', legend = False)
#plt.show()


#fig = px.box(infeccoes_estado_2023, y = 'qtd_infeccoes', title = 'Boxplot de infeccções por Estado / 2023')
#fig.show()

#print("Gráfico criado!")
#personalizar o grafico
#plt.title('Quantidade de infecções por ano', fontsize = 14)
#plt.title('Boxplot de infeccções por Estado / 2023', fontsize = 14)
#plt.xlabel('Ano', fontsize = 12)
#plt.ylabel('Quantidade de infecções', fontsize = 12)
#plt.grid(axis='y', linestyle ='--', alpha = 0.7)

#comparação, utilizar gráfico de barras
#ordenar do maior para o menor

infeccoes_2023 = infeccoes_estado_2023.sort_values(by = 'qtd_infeccoes', ascending = False)


# grafico normal 
#plt.figure(figsize=(10,6))
#sns.barplot(data = infeccoes_2023, x = 'uf', y = 'qtd_infeccoes', hue = 'uf', palette='viridis', legend = False )
#plt.title('Quantidade de infeccções por Estado em 2023', fontsize = 14)
#plt.xlabel('Estado', fontsize = 12)
#plt.ylabel('Quantidade de Infecções', fontsize = 12)
#plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
#plt.show()

#grafico de tendencia 
plt.figure(figsize=(10,6))
sns.regplot(data = infeccoes_estado, x='ano', y='qtd_infeccoes', scatter_kws={"s":15}, line_kws={"color":"red"})
plt.title('Tendência das infeccções ao longo dos anos', fontsize = 14)
plt.xlabel('Ano', fontsize = 12)
plt.ylabel('Quantidade de Infecções', fontsize = 12)
plt.grid(True)
plt.show()