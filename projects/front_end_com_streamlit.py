from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/front_end_com_streamlit")

st.subheader("Front end com Streamlit")

if 'descricao_project2' not in st.session_state:
    st.session_state['descricao_project2'] = """
Descrição:
Painel administrativo desenvolvido com Streamlit que consome uma REST API para gestão completa de uma cafeteria.
Foco em eficiência operacional, experiência do usuário e facilidade de integração em ambientes corporativos.

Destaques técnicos:
- Stack: Python + Streamlit; comunicação via JSON sobre REST API.
- Arquitetura modular: componentes reutilizáveis, separação de responsabilidades e testes unitários/integrados.
- Performance: chamadas assíncronas, cache local e paginação para reduzir latência e uso de banda.
- Validação e segurança: validação de entrada (pydantic ou validação customizada), tratamento robusto de erros e feedback claro ao usuário.
- Operações de mídia: suporte a upload e otimização de imagens; armazenamento preparado.
- Observabilidade: logs de ações administrativas e mensuração de métricas para auditoria.
- Deploy: pronto para empacotar em Docker e orquestrar via Kubernetes; adequado para pipelines CI/CD.

Funcionalidades principais:
- CRUD completo para tipos de café, descrições, companhias e avaliações.
- Upload de imagens, paginação, filtros avançados e busca.
- Exportação de dados (CSV/XLSX) e integração com ferramentas de BI.
- Dashboards analíticos com gráficos (ex.: vendas, avaliações, inventário, KPIs).
- Confirmações, logs visíveis e suporte básico a permissões/roles.

Valor comercial:
Ferramenta pronta para acelerar operações de gestão de produtos e marketing, 
reduzir retrabalho manual e fornecer insights acionáveis para tomada de decisão. 
Implementação pensada para integração com sistemas corporativos e escalabilidade em infraestrutura cloud.
"""

if 'fotos_project2' not in st.session_state:
    fotos = list(assets_path.glob("*.png"))
    st.session_state['fotos_project2'] = [Image.open(foto) for foto in fotos]

st.write(st.session_state['descricao_project2'])

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in st.session_state['fotos_project2']:
    st.image(foto, caption=foto.filename, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/front_end_streamlit"
)
