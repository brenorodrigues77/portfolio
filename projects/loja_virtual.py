from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/loja_virtual")

st.subheader("Loja Virtual")

if 'descricao' not in st.session_state:
    st.session_state['descricao'] = ("""
    - Projeto desenvolvido em linguagem Javascript, usando o framework NodeJs,
    - aplicação com menu de itens da loja, adicionando itens, carrrinho interativo, opçoes de remover, menu de endereço, check out e historico de compras.
    """)

if 'fotos' not in st.session_state:
    fotos = list(assets_path.glob("*.png"))
    st.session_state['fotos'] = [Image.open(foto) for foto in fotos]

st.write(st.session_state['descricao'])

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in st.session_state['fotos']:
    st.image(foto, caption=foto.filename, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/lojaVirtual"
)
