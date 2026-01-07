import streamlit as st
import base64
from pathlib import Path

# ==============================
# CONFIGURAÇÃO INICIAL
# ==============================
st.set_page_config(layout="wide")

st.markdown("""
<style>

/* ==============================
   BLOQUEAR MODO ESCURO DO SISTEMA
   ============================== */

/* Força modo claro */
:root {
    color-scheme: light;
}

/* App inteiro */
.stApp {
    background-color: #FDF5E6 !important;
    color: #2e2e2e !important;
}

/* Texto padrão do Streamlit */
html, body, [class*="css"] {
    color: #2e2e2e !important;
}

/* Títulos */
h1, h2, h3, h4, h5, h6 {
    color: #2e2e2e !important;
}

/* Parágrafos e textos */
p, span, div, label {
    color: #4a4a4a !important;
}

/* Inputs */
input, textarea, select {
    background-color: #ffffff !important;
    color: #2e2e2e !important;
}

/* Métricas */
[data-testid="stMetricValue"] > div {
    color: #2e2e2e !important;
}

[data-testid="stMetricLabel"] > div {
    color: #4a4a4a !important;
}

/* Ignora modo escuro do sistema */
@media (prefers-color-scheme: dark) {
    html, body, .stApp {
        background-color: #FDF5E6 !important;
        color: #2e2e2e !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ==============================
# FONTE WONDERFUL BRANDING
# ==============================
font_path = Path("assets/fonts/WonderfulBranding.ttf")

with open(font_path, "rb") as f:
    wonderful_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
<style>

/* ==============================
   FONTES
   ============================== */

@font-face {{
    font-family: 'WonderfulBranding';
    src: url(data:font/ttf;base64,{wonderful_base64}) format('truetype');
}}

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded');

/* ==============================
   TÍTULOS
   ============================== */

h1 {{
    font-family: 'WonderfulBranding', serif !important;
    font-size: 30px !important;
    letter-spacing: 0.08em !important;
    text-align: center !important;
    margin-bottom: 30px !important;
}}

# h2, h3, h4, h5, h6,
# p, label {{
#     font-family: 'Cormorant Garamond', serif !important;
# }}

/* ==============================
   CORREÇÃO DEFINITIVA DOS ÍCONES
   ============================== */

[data-testid="stIconMaterial"] {{
    font-family: "Material Symbols Rounded" !important;
    font-variation-settings:
        'FILL' 0,
        'wght' 400,
        'GRAD' 0,
        'opsz' 24;
    font-size: 24px !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&display=swap');

/* SIDEBAR */
[data-testid="stSidebar"] { 
    background-color: 	#FDF5E6 !important; 
    font-family: 'Cormorant Garamond', serif !important;
}

/* LINKS DO MENU */
[data-testid="stSidebar"] a {
    font-family: 'Cormorant Garamond', serif !important;
    color: #4a4a4a !important;
    font-size: 100px !important;
    text-decoration: none !important;
    transition: 0.3s ease !important;
    padding-left: 4px !important;
}

/* HOVER */
[data-testid="stSidebar"] a:hover {
    color: #F5DEB3 !important;
    letter-spacing: 0.03em !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# FUNDO DA PÁGINA
# -----------------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---- DEFINA A IMAGEM ----
add_bg_from_local("images/layout/fundomake.jpg")

# -----------------------------------
# CONTEÚDO DA PÁGINA
# -----------------------------------
st.title("Cabelo e Maquiagem")


st.markdown(
    """
    <style>
        .texto-cerimonia {
            width: 100%;
            padding: 35px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.80);
            backdrop-filter: blur(6px);
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            font-family: 'Cormorant Garamond', serif;
            font-size: 18px;
            line-height: 1.8;
        }

        .texto-cerimonia > div {
            margin-bottom: 1rem;
        }

        .texto-cerimonia > div:last-child {
            margin-bottom: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="texto-cerimonia"> 
    <div>Para o nosso grande dia, optamos por uma produção especial que combine com a essência do casamento!!</div>
    <div>Queremos que todos se sintam confortáveis e confiantes, então não há regras. O mais importante é celebrar conosco e aproveitar cada momento.</div>
    <div>Portanto deixaremos as seguintes sugestões de lugares: 
    </div>
    """,
    unsafe_allow_html=True
)
