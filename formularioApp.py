import streamlit as st

# Valores default (opcional)
nome = ''
preco = 0.00
estoque = 10

# Configurações da Aba da Página
st.set_page_config(
 page_title="Cadastro de Produtos", # Título da aba
 page_icon=":shopping_trolley:", # Ícone da aba (opcional)
 #layout="wide" # Layout largo (opcional)
)

# Conteúdo da aplicação
st.title("Cadastrar")
st.subheader("Formulário para cadastrar produtos")

# Cria formulário
with st.form(key='form_produto'):
 nome = st.text_input('Nome do Produto', max_chars=60, value=nome,
 placeholder="Nome com descrição do produto")
 preco = st.number_input('Preço do Produto', min_value=0.00, step=0.01, value = preco)
 estoque = st.number_input('Quantidade em Estoque', min_value=0, step=1, value=estoque)
 # True ou False
 enviou = st.form_submit_button(label='Cadastrar')

# Ação quando o formulário é submetido
if enviou:
 if not nome:
    st.warning(f'Campo "nome" é obrigatório!')
else:
 st.success(f'Produto cadastrado com sucesso!')
 st.write(f'**Nome:** {nome}')
 st.write(f'**Preço:** R$ {preco:.2f}')
 st.write(f'**Quantidade em estoque:** {estoque}') 