from PIL import Image
from pathlib import Path
import streamlit as st

assets_path = Path("assets/loja_virtual")

st.subheader("Loja Virtual")

if 'descricao_project3' not in st.session_state:
    st.session_state['descricao_project3'] = ("""
    Descrição:
Loja Virtual é uma aplicação de comércio eletrônico desenvolvida em JavaScript com NodeJs, com interface intuitiva para navegação de produtos, seleção e gerenciamento de carrinho, processo de checkout e histórico de compras. Interface responsiva e preparada para integração com APIs de pagamento e serviços de backend.

Destaques técnicos:
- Arquitetura modular: separação clara entre camadas de apresentação e lógica de negócio, facilitando manutenção e testes.
- Gerenciamento de estado do carrinho: operações de adicionar, editar e remover itens com persistência local (localStorage / session) e sincronização com backend.
- Fluxo de checkout: capturas de dados de endereço, validações de formulário, cálculo de frete e resumo de pedido.
- Mídia e performance: carregamento otimizado de imagens, lazy loading e suporte a diferentes resoluções.
- Integrações futuras: pontos de extensão para gateways de pagamento, serviços de estoque e sistemas de notificação.
- Pronto para deploy: configuração compatível com conteinerização (Docker) e pipelines CI/CD.

Funcionalidades principais:
- Catálogo de produtos com filtros e busca.
- Carrinho interativo com atualização de quantidades e remoção de itens.
- Tela de checkout com validação de endereço e resumo do pedido.
- Histórico de compras com detalhes e status.

Valor comercial:
Protótipo pronto para validação de produto (MVP) que acelera lançamentos de lojas online, reduz atrito na jornada de compra e aumenta conversão com UX focada. Código estruturado para escalar em ambientes corporativos e integrar rapidamente com ferramentas de pagamento e logística.
""")

if 'fotos_project3' not in st.session_state:
    fotos = list(assets_path.glob("*.png"))
    st.session_state['fotos_project3'] = [Image.open(foto) for foto in fotos]

st.write(st.session_state['descricao_project3'])

st.write("Fotos")
# Exiba as fotos no Streamlit
for foto in st.session_state['fotos_project3']:
    st.image(foto, caption=foto.filename, use_container_width=True)

st.link_button(
    "Codigo Fonte",
    "https://github.com/brenorodrigues77/lojaVirtual"
)
