import streamlit as st
import pandas as pd

# Cria um dicionário para simulação dos dados
dados = {
 'Nome do Produto': ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador'],
 'Descrição': ['Teclado mecânico', 'Mouse sem fio', 'Monitor 24 polegadas',
 'Placa mãe ATX', 'Processador i7'],
 'Preço': [199.99, 99.99, 899.99, 499.99, 1299.99],
 'Quantidade em Estoque': [10, 15, 5, 8, 12]
}

# Converte dicionário em DataFrame
df1 = pd.DataFrame(dados)

# Título do aplicativo
st.title('Lista de Produtos')

# Exibe o DataFrame
st.subheader('DataFrame a partir do dicionário de dados')
st.dataframe(df1)

# Define URL do arquivo de Excel
url = 'https://softgraf.com/cursodatascience/produtos.xlsx'

# Lê o arquivo da url e converte em um DataFrame
df2 = pd.read_excel(url, engine='openpyxl')

# Exibe o DataFrame
st.subheader('DataFrame a partir do arquivo de Excel')
st.dataframe(df2)