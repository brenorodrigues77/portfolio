import streamlit as st

st.set_page_config(layout="wide")

about_me = st.Page(
    page="home/about_me.py",
    title="Sobre mim",
    icon="👨🏻",
    default=True,
)

project_1 = st.Page(
    page="projects/pergunte_me.py",
    title="Pergunte-me",
    icon="👨🏻‍💻",
)

project_2 = st.Page(
    page="projects/front_end_com_streamlit.py",
    title="Front end com Streamlit",
    icon="👨🏻‍💻",
)

page = st.navigation(
    {
        "Informações": [about_me],
        "Projetos": [project_1, project_2],
    }
)

page.run()
