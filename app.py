import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="ARP — Dashboard Gerencial",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Esconde o menu/rodapé padrão do Streamlit pra deixar o dashboard ocupar a tela toda
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Proteção por chave de acesso na URL (?chave=prodentis2026) ──
params = st.query_params
CHAVE_CORRETA = "prodentis2026"
chave_informada = params.get("chave", "")

if chave_informada != CHAVE_CORRETA:
    st.title("🔒 Acesso restrito")
    st.write("Adicione `?chave=SUACHAVE` no final do link para acessar o dashboard.")
    st.stop()

# ── Carrega e exibe o dashboard HTML ──
HTML_PATH = os.path.join(os.path.dirname(__file__), "Dashboard_ADM.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1400, scrolling=True)
