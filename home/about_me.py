import streamlit as st
from PIL import Image

perfil_img = "./assets/perfil/perfil.jpg"


col1, col2 = st.columns([1, 5])
with col1:
    st.image(Image.open(perfil_img), use_container_width=150)
with col2:
    st.title(" Desenvolvedor Jr | Backend | Python | SQL | Inteligência Artificial ")

st.write(
    """
        -  🚀 Desenvolvedor Jr | Impulsionando a Inovação com Dados e IA

        -  Com 1 ano e 8 meses de experiência em Python, transformo desafios em soluções inteligentes e escaláveis, com proficiência em Backend.

        -  Sou um entusiasta da Inteligência Artificial e Machine Learning, focado em desenvolver Agentes de IA e sistemas guiados por dados que trazem autonomia e eficiência às aplicações Web.

        Minhas ferramentas e habilidades incluem:
        
        - 🌐 Django e Django REST Framework: Construção de backends robustos para sustentar soluções de IA no desenvolvimento web.
        - 🤖 Inteligência Artificial: Criação de agentes e Integrações via APIs em aplicações web para automações e agentes autônomos.
        - 🗄️ SQL e PostgreSQL: Expertise em ETL e otimização de consultas para gestão de dados.
        - 📊 Pandas e NumPy: Extraio valor e insights de grandes volumes de dados.
        -  Git, GitHub, GitLab e Bitbucket: Versionamento e colaboração eficaz em projetos de desenvolvimento.
        -  Metodologias Ágeis: Experiência em Scrum, Kanban e Jira para entrega contínua de valor.

        Aprendizados Constantes:

        - 🧠 TensorFlow e Keras: Para arquitetar e treinar modelos de IA de ponta.
        - 💡 Scikit-learn: Aplicação estratégica de algoritmos de Machine Learning.
        - 🖼️ Pillow: Para manipulação e pré-processamento de imagens em Visão Computacional.

    """
)

st.write("\n")
st.subheader("Experiencia Profissional")

st.write(
    """
        -   integração de Inteligência artificial a aplicações web.
        -   Desenvolvimento de agentes de IA para automação de tarefas manuais.
        -   Desenvolvimento de backend com Django e Django REST Framework. 
        -   Criador de APIs RESTful com Django REST Framework.
        -   Tratamento de dados com Pandas, Numpy e SQL para envio a banco de dados relacionais.
        -   Analista de dados com métricas de CRM. 
        -   Desenvolvimento de interfaces web com Streamlit.
        -   Habilidade em SQL e PostgreSQL para gestão de dados.
        -   Versionamento de código com Git e GitHub.
    """
)

st.link_button("Linkedin", "https://www.linkedin.com/in/breno7/")
st.link_button("Github", "https://github.com/brenorodrigues77")
