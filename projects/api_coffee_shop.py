from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/api_coffee_shop")

st.subheader("API Coffee Shop")

if 'descricao_project4' not in st.session_state:
    st.session_state['descricao_project4'] = """
Descrição:
- API Coffee Shop, Um projeto construído utilizando o Django e Django REST Framework com objetivo de trazer informações de menu, fazer pedidos e balanço de consumos.
        
Funcionalidades: 
- Descrição: Este projeto é um painel de administração para gerenciar dados de cafés incluindo:
- Gerar um token de acesso aos usuarios da aplicação.
- Visualizar Menu de cafes, 
- Visualizar pedidos pendentes dos clientes. 
- acompanhar balanço de consumo por data. 
- Os endpoints são construídos utilizando Django e Django REST Framework para interagir com os dados.

Funcionalidades:

- Visualizar a lista de opções de cafés.
- Realizar o pedido de cafes.
- Ver pedidos pendentes dos clientes.
- Ver o balanço de consumos dos ingredientes atraves de uma data futura.
"""

if 'fotos_project4' not in st.session_state:
    fotos = list(assets_path.glob("*.png"))
    st.session_state['fotos_project4'] = [Image.open(foto) for foto in fotos]

st.write(st.session_state['descricao_project4'])

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in st.session_state['fotos_project4']:
    st.image(foto, caption=foto.filename, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/api_coffee_shop"
)
