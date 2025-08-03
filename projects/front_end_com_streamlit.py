from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/front_end_com_streamlit")

st.subheader("Front end com Streamlit")

st.write("""
Descrição:
- Front end com Streamlit, Um projeto construído utilizando o framework Streamlit consumindo um API rest de uma cafeteria.
        
Funcionalidades: 
- Descrição: Este projeto é um painel de administração para gerenciar dados de cafés incluindo:
- tipos de cafés, 
- descrições de cafés, 
- companhias de cafés e avaliações de cafés. 
- O painel é construído utilizando a biblioteca Streamlit e utiliza APIs para interagir com os dados.

Funcionalidades:

- Gerenciamento de tipos de cafés 
- Gerenciamento de descrições de cafés 
- Gerenciamento de companhias de cafés 
- Gerenciamento de avaliações de cafés

Visualização de estatísticas de companhias de cafés
""")

fotos = list(assets_path.glob("*.png"))

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in fotos:
    img = Image.open(foto)
    st.image(img, caption=foto.name, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/front_end_streamlit"
)
