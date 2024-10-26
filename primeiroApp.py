import streamlit as st

# Título de página
st.title("Primeiro App :sunglasses:")
st.image('https://www.softgraf.com/icones/logo_softgraf.png', width=200)
st.header('Este é um header com um divisor', divider='rainbow')
st.subheader('Este é um subheader: _Streamlit_ é :blue[legal]')
st.write('Este é um *Texto* comum')
"Texto Mágico!"
texto = "Texto na Variável"
texto
x = 10
'x', x
st.markdown("Markdown: *Streamlit* é **realmente** ***legal***.")
st.markdown('''
 :red[Streamlit] :orange[pode] :green[escrever] :blue[texto] :violet[em]
 :gray[muitas] :rainbow[cores] e :blue-background[texto destacado].
''')
multi = '''Se terminar a linha com dois espacos,
uma quebra de linha suave é usada para a próxima linha.
Dois ou mais "ENTER" resulta em apenas uma quebra de linha.
'''

st.markdown(multi)
st.text_input('Nome:')
st.number_input('Preço:')
st.text_area('Descrição:')
#chat fica fixo na parte inferior da tela

prompt = st.chat_input("Digite alguma coisa")

if prompt:
    st.write(':red[Usuário enviou o seguinte prompt:]', prompt)
st.slider("Qual sua idade?", 0, 120, 25)

opcoes = st.multiselect("Selecione suas cores favoritas",
 ["Verde", "Amarelo", "Vermelho", "Azul"], #lista de cores
 ["Amarelo", "Vermelho"] #seleção padrão
 )
"Cores selecionadas:"
st.write(opcoes)


genero = st.radio("Escolha seu gênero de filme favorito",
 [":rainbow[Comédia]", "***Drama***", "Documentário :movie_camera:"],
 index=None,
 )

st.write("Você escolheu:", genero)

opcao = st.selectbox("Como gostaria de ser contactado?", ("Email", "Telefone", "Whatsapp"))
cidades = ['Ponta Grossa', 'Curitiba', 'Castro', 'Carambeí', 'Piraí do Sul']
padroes = ['Curitiba', 'Castro', 'Carambeí']

with st.expander('Expander cidades'):
 escolhidas = st.multiselect('Selecione as cidades', cidades, padroes)
st.write("Cidades escolhidas:", escolhidas) 

# Barra lateral
with st.sidebar:
 mensagens = st.container(height=300)
 #'operador morsa' := (a partir do python 3.8)
 if prompt := st.chat_input('Digite algo:'):
    mensagens.chat_message('usuario').write(prompt)
 mensagens.chat_message('assistente').write(f'Echo: {prompt}')