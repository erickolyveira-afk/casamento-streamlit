import streamlit as st
import os
import pandas as pd
import base64
from pathlib import Path

# --------------------------------------
# RSVP
# --------------------------------------

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

# ======================================================
# FUNDO DA PÁGINA — MOBILE E DESKTOP
# ======================================================
def add_responsive_background(desktop_img, mobile_img):
    import base64

    with open(desktop_img, "rb") as f:
        desktop_base64 = base64.b64encode(f.read()).decode()

    with open(mobile_img, "rb") as f:
        mobile_base64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        /* DESKTOP / NOTEBOOK */
        .stApp {{
            background-image: url("data:image/jpeg;base64,{desktop_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* MOBILE */
        @media (max-width: 768px) {{
            .stApp {{
                background-image: url("data:image/jpeg;base64,{mobile_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

add_responsive_background(
    desktop_img="images/layout/Floripa 311224.jpg",
    mobile_img="images/layout/Floripa 311223.jpg"
)

# Caminho da fonte Wonderful Branding
font_path = Path("assets/fonts/WonderfulBranding.ttf")

# Converte fonte para base64
with open(font_path, "rb") as f:
    wonderful_font = f.read()
wonderful_base64 = base64.b64encode(wonderful_font).decode()

st.markdown(f"""
<style>

    @font-face {{
        font-family: 'WonderfulBranding';
        src: url(data:font/ttf;base64,{wonderful_base64}) format('truetype');
    }}

    /* TÍTULOS COM WONDERFUL BRANDING */
    h1 {{
        font-family: 'WonderfulBranding', serif !important;
        font-size: 60px !important;   /* 👈 AQUI VOCÊ AJUSTA */
        font-weight: 100 !important;
        letter-spacing: 0.05em !important;
        text-align: center !important;
    }}

    h2, h3, h4, h5, h6 {{
        font-family: 'WonderfulBranding', serif !important;
        font-size: 27px !important;   /* 👈 Ajuste aqui se quiser */
        font-weight: 100 !important;
        letter-spacing: 0.05em !important;
        text-align: left !important;
    }}

    /* Labels dos inputs */
    label, .stTextInput label, .stNumberInput label, .stSelectbox label {{
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 20px !important;
        font-weight: 300 !important;
        letter-spacing: 0.03em !important;
    }}

</style>
""", unsafe_allow_html=True)

st.header("Confirme aqui a sua presença:")

name = st.text_input("Seu nome:")
confirmation = st.selectbox("Você confirma presença?", ["Sim", "Não"])

csv_path = "rsvp.csv"

# Cria CSV caso não exista
if not os.path.exists(csv_path):
    pd.DataFrame(columns=["nome", "confirmacao"]).to_csv(csv_path, index=False)

if st.button("Enviar resposta"):
    if name:
        df = pd.read_csv(csv_path)
        df.loc[len(df)] = [name, confirmation]
        df.to_csv(csv_path, index=False)
        st.success(f"Obrigado, {name}! Sua resposta foi registrada.")
    else:
        st.error("Por favor, insira seu nome antes de enviar.")

