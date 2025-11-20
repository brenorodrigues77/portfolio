from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/pergunte_me")

st.subheader("Pergunte-me")

if 'descricao_project1' not in st.session_state:
    st.session_state['descricao_project1'] = """
Descrição:
Pergunte-me é um assistente de perguntas e respostas baseado em Recuperação Augmentada por Documentos (RAG), construído com Streamlit e LangChain para oferecer buscas contextuais e respostas extraídas de arquivos locais e URLs da web.

Destaques técnicos:
- Arquitetura: ingestão de documentos com chunking e metadados, indexação por embeddings e busca vetorial (FAISS/Chroma/Milvus compatíveis).
- Modelos e provedores: suporte a múltiplos provedores de LLMs e chaves de API, rotas de fallback e controle de custos.
- Fontes suportadas: PDF, TXT, CSV, páginas web e vídeos (transcrição de YouTube); processamento assíncrono e pré-processamento de texto.
- Pipeline: carregadores de documentos, limpeza, geração de embeddings, armazenagem vetorial e mecanismo de recuperação + ranking.
- Experiência: interface intuitiva para upload, histórico de conversa, visualização de trechos de origem (source citations) e exportação de respostas.
- Confiabilidade e observabilidade: logs de ingestão, métricas de uso, cache e tolerância a falhas.
- Segurança e privacidade: opção de processamento local de documentos, controle de chaves, e preparação para políticas de conformidade (ex.: anonimização de metadados).

Funcionalidades comerciais:
- Redução do tempo de pesquisa interna e suporte ao cliente com respostas rápidas e precisas.
- Integração simples com fluxos corporativos e sistemas de conhecimento existentes.
- Escalável para proof-of-concept até produção com Docker e pipelines CI/CD.
- Pronto para customizações empresariais: regras de negócio, permissões e auditoria.
"""

if 'fotos_project1' not in st.session_state:
    fotos = list(assets_path.glob("*.png"))
    st.session_state['fotos_project1'] = [Image.open(foto) for foto in fotos]

st.write(st.session_state['descricao_project1'])

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in st.session_state['fotos_project1']:
    st.image(foto, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/pergunte_me"
)
