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
DIR = os.path.dirname(__file__)
HTML_PATH = os.path.join(DIR, "Painel_ADM.html")

# Se o nome mudar de novo no futuro, procura o primeiro .html na pasta como fallback
if not os.path.exists(HTML_PATH):
    html_files = [f for f in os.listdir(DIR) if f.lower().endswith(".html")]
    if html_files:
        HTML_PATH = os.path.join(DIR, html_files[0])
    else:
        st.error(f"Nenhum arquivo .html encontrado na pasta do app ({DIR}).")
        st.stop()

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1400, scrolling=True)
