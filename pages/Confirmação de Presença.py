import streamlit as st
import base64
from pathlib import Path
import pandas as pd

from google.oauth2.service_account import Credentials
import gspread

# ======================================================
# CONFIGURAÇÃO GOOGLE SHEETS
# ======================================================

SHEET_URL = "https://docs.google.com/spreadsheets/d/SEU_ID_DA_PLANILHA_AQUI"

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

gc = gspread.authorize(credentials)
sheet = gc.open_by_url(SHEET_URL).sheet1


# ======================================================
# CSS — SIDEBAR
# ======================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&display=swap');

[data-testid="stSidebar"] { 
    background-color: #FDF5E6 !important; 
    font-family: 'Cormorant Garamond', serif !important;
}

[data-testid="stSidebar"] a {
    font-family: 'Cormorant Garamond', serif !important;
    color: #4a4a4a !important;
    font-size: 18px !important;
    text-decoration: none !important;
    transition: 0.3s ease !important;
}

[data-testid="stSidebar"] a:hover {
    color: #F5DEB3 !important;
    letter-spacing: 0.03em !important;
}

</style>
""", unsafe_allow_html=True)


# ======================================================
# BLOQUEAR MODO ESCURO
# ======================================================

st.markdown("""
<style>

:root {
    color-scheme: light;
}

.stApp {
    background-color: #FDF5E6 !important;
    color: #2e2e2e !important;
}

html, body, [class*="css"] {
    color: #2e2e2e !important;
}

input, textarea, select {
    background-color: #ffffff !important;
    color: #2e2e2e !important;
}

@media (prefers-color-scheme: dark) {
    html, body, .stApp {
        background-color: #FDF5E6 !important;
        color: #2e2e2e !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ======================================================
# FUNDO RESPONSIVO
# ======================================================

def add_responsive_background(desktop_img, mobile_img):
    with open(desktop_img, "rb") as f:
        desktop_base64 = base64.b64encode(f.read()).decode()

    with open(mobile_img, "rb") as f:
        mobile_base64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/jpeg;base64,{desktop_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        @media (max-width: 768px) {{
            .stApp {{
                background-image: url("data:image/jpeg;base64,{mobile_base64}");
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


# ======================================================
# FONTE PERSONALIZADA
# ======================================================

font_path = Path("assets/fonts/WonderfulBranding.ttf")

with open(font_path, "rb") as f:
    font_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
<style>

@font-face {{
    font-family: 'WonderfulBranding';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}

h1 {{
    font-family: 'WonderfulBranding', serif !important;
    font-size: 60px !important;
    font-weight: 100 !important;
    letter-spacing: 0.05em !important;
    text-align: center !important;
}}

label {{
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 20px !important;
}}

</style>
""", unsafe_allow_html=True)


# ======================================================
# FORMULÁRIO RSVP
# ======================================================

st.header("Confirme aqui a sua presença:")

nome = st.text_input("Seu nome completo:")
confirmacao = st.selectbox(
    "Você confirma presença?",
    ["Sim", "Não"]
)

if st.button("Enviar resposta"):

    if not nome.strip():
        st.error("Por favor, informe seu nome.")
    else:
        sheet.append_row([
            nome,
            confirmacao
        ])

        st.success("💛 Obrigado! Sua resposta foi registrada com sucesso.")