import streamlit as st
from PIL import Image

perfil_img = "./assets/perfil/perfil.jpg"


col1, col2 = st.columns([1, 5])
with col1:
    st.image(Image.open(perfil_img), use_container_width=150)
with col2:
    st.title("Analista de Dados Jr | Python | SQL | Excel | Streamlit")

st.write(
    """
        -  Com experiência em Python, SQL, Excel e Streamlit, atuo na análise, visualização e interpretação de dados para apoiar a tomada de decisões estratégicas.

        -  Transformando Dados em Insights Valiosos, busco extrair informações relevantes e gerar valor para o negócio por meio de dashboards, relatórios e automações de processos.

        Minhas ferramentas e habilidades incluem:
        
        - 📊 Streamlit: Criação de dashboards interativos e relatórios dinâmicos para visualização de dados.
        - 🗄️ SQL e PostgreSQL: Manipulação, extração e análise de dados em bancos relacionais.
        - 🐍 Python: Automação de tarefas, análise de dados com Pandas e NumPy.
        - 📈 Excel: Modelagem, tratamento e análise de dados.
        -  Git e GitHub: Versionamento e colaboração em projetos de dados.

        Aprendizados Constantes:

        - 🧠 TensorFlow e Keras: Para arquitetar e treinar modelos de IA de ponta.
        - 💡 Scikit-learn: Aplicação estratégica de algoritmos de Machine Learning.

    """
)

st.write("\n")
st.subheader("Experiencia Profissional")

st.write(
    """
        - Análise e visualização de dados para geração de insights de negócio.
        - Criação de dashboards e relatórios interativos em Power BI e Streamlit.
        - Manipulação, extração e tratamento de dados com SQL, Pandas e Excel.
        - Automação de processos e rotinas de dados utilizando Python.
        - Experiência em versionamento de projetos de dados com Git e GitHub.
    """
)


