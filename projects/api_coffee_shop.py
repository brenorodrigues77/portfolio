from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/api_coffee_shop")

st.subheader("API Coffee Shop")

if 'descricao_project4' not in st.session_state:
    st.session_state['descricao_project4'] = """
API Coffee Shop — Plataforma backend escalável para operações de cafeteria

Visão geral:
API Coffee Shop é uma API RESTful desenvolvida com Django e Django REST Framework, projetada para gerenciar de forma confiável o catálogo de produtos, o fluxo de pedidos, o inventário e os relatórios operacionais de uma cafeteria. A solução prioriza segurança, observabilidade e integração simples com clientes web e mobile.

Principais recursos técnicos:
- API RESTful versionada para cardápio, pedidos, clientes e inventário.
- Autenticação baseada em tokens / JWT com controle de permissões (admin, barista, cliente).
- Modelagem relacional e migrações preparadas para bancos como PostgreSQL.
- Serializers e validações robustas para garantir integridade dos dados.
- Paginação, filtros e ordenação em endpoints de listagem; suporte a upload e entrega de imagens.
- Estrutura orientada a testes (unit + integração) e fácil instrumentação para monitoramento (logs, health-checks, métricas).

Benefícios comerciais:
- Redução de desperdício e custo através de relatórios de consumo por período e visão de reabastecimento.
- Acelera o tempo de integração com apps de delivery e sistemas PDV, permitindo novas fontes de receita.
- Melhora a eficiência operacional com rastreabilidade de pedidos e gerenciamento de filas/pedidos pendentes.
- Arquitetura modular que facilita customizações para redes de cafeterias (promoções, fidelidade, dashboards).

Stack e implantação recomendada:
- Python 3.x, Django, Django REST Framework
- Banco relacional (PostgreSQL em produção; SQLite em dev)
- Autenticação JWT/DRF, Gunicorn + Nginx, containerização com Docker e pipelines CI/CD
- Testes automatizados (pytest/django) e scripts de migração

Pronto para POC e customizações comerciais sob demanda.
"""

if 'fotos_project4' not in st.session_state:
    fotos = list(assets_path.glob("*.png"))
    st.session_state['fotos_project4'] = [Image.open(foto) for foto in fotos]

st.write(st.session_state['descricao_project4'])

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in st.session_state['fotos_project4']:
    st.image(foto, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/api_coffee_shop"
)
