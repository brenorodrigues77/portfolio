from PIL import Image
from pathlib import Path
import streamlit as st


from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/pergunte_me")

st.subheader("Pergunte-me")

st.write("""
Descrição:
- Pergunte-me é um projeto de chatbot que utiliza a tecnologia de linguagem natural para responder tudo sobre um determinado arquivo do seu computador ou urls da internet. O projeto é construído utilizando o framework Streamlit e a biblioteca Langchain para processamento de linguagem natural.
         
Funcionalidades: 
- Resposta a perguntas dos usuários utilizando modelos de linguagem natural 
- Suporte a diferentes tipos de arquivos (Site, Youtube, PDF, CSV, TXT) Interface de usuário simples e intuitiva.
- Tecnologias utilizadas: Streamlit Langchain Python
- Suporte a varias chaves de APIs de inteligencia artificial.
""")

fotos = list(assets_path.glob("*.png"))

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in fotos:
    img = Image.open(foto)
    st.image(img, caption=foto.name, use_container_width=True)
