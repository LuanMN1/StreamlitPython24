import streamlit as st
import pandas as pd

# Set up the page configuration
st.set_page_config(
    page_title="Controle de Estoque",
    page_icon=":shopping_trolley:",
)

# Initialize the DataFrame in session state
if 'produtos' not in st.session_state:
    st.session_state['produtos'] = pd.DataFrame(columns=['ID', 'Nome', 'Preco', 'Estoque'])

# Function to add a new product
def cadastra_produto():
    produto_id = st.text_input("ID")
    produto_nome = st.text_input("Nome")
    produto_preco = st.number_input("Preço", min_value=0.0)
    produto_estoque = st.number_input("Estoque", min_value=0)

    if st.button("Cadastrar Produto"):
        novo_produto = pd.DataFrame({
            'ID': [produto_id],
            'Nome': [produto_nome],
            'Preco': [produto_preco],
            'Estoque': [produto_estoque]
        })

        # Add the new product to the existing DataFrame
        st.session_state['produtos'] = pd.concat([st.session_state['produtos'], novo_produto], ignore_index=True)
        st.success("Produto cadastrado com sucesso!")

# Function to alter an existing product
def alterar_produto():
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox("Selecione ID do Produto para Alterar", lista_produtos)
    
    if produto_id:
        # Locate the product by ID
        produto = st.session_state['produtos'][st.session_state['produtos']['ID'] == produto_id].iloc[0]
        
        # Input fields to update the product
        novo_nome = st.text_input("Nome", value=produto['Nome'])
        novo_preco = st.number_input("Preço", min_value=0.0, value=produto['Preco'])
        novo_estoque = st.number_input("Estoque", min_value=0, value=int(produto['Estoque']))
        
        if st.button("Atualizar Produto"):
            # Update the information in the DataFrame
            st.session_state['produtos'].loc[st.session_state['produtos']['ID'] == produto_id, ['Nome', 'Preco', 'Estoque']] = [novo_nome, novo_preco, novo_estoque]
            st.success("Produto atualizado com sucesso!")

# Function to delete a product
def apagar_produto():
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox("Selecione ID do Produto para Apagar", lista_produtos)
    
    if produto_id:
        if st.button("Apagar Produto"):
            # Remove the product by ID
            st.session_state['produtos'] = st.session_state['produtos'][st.session_state['produtos']['ID'] != produto_id]
            st.success("Produto apagado com sucesso!")

# Function to list all products
def listar_produtos():
    st.subheader("Todos os Produtos do Sistema")
    st.dataframe(st.session_state['produtos'])

# Main Program
if __name__ == "__main__":
    st.title("Controle de Estoque")

    # Sidebar for action control
    opcao = st.sidebar.selectbox("Escolha uma opção",
                                  ["Cadastrar Produto", "Alterar Produto", "Apagar Produto", "Listar Todos os Produtos"])
    
    if opcao == "Cadastrar Produto":
        cadastra_produto()
    elif opcao == "Alterar Produto":
        alterar_produto()
    elif opcao == "Apagar Produto":
        apagar_produto()
    elif opcao == "Listar Todos os Produtos":
        listar_produtos()