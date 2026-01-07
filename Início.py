import streamlit as st
from datetime import date
import pandas as pd
import os
import qrcode
from io import BytesIO
import base64
from pathlib import Path

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&display=swap');

/* SIDEBAR */
[data-testid="stSidebar"] { 
    background-color: #FDF5E6 !important; 
    font-family: 'Cormorant Garamond', serif !important;
}

/* LINKS DO MENU */
[data-testid="stSidebar"] a {
    font-family: 'Cormorant Garamond', serif !important;
    color: #363636 !important;
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

# --------------------------------------
# Configurações da página
# --------------------------------------

# ----- FUNDO DA PÁGINA -----
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
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("images/layout/Floripa 311223.jpg")

st.set_page_config(page_title="Nosso Casamento", page_icon="💍", layout="wide")

# Caminho da fonte Wonderful Branding
font_path = Path("assets/fonts/WonderfulBranding.ttf")

# Converte fonte para base64
with open(font_path, "rb") as f:
    wonderful_font = f.read()
wonderful_base64 = base64.b64encode(wonderful_font).decode()

st.markdown(f"""
    <style>

    /* Registrar a fonte Wonderful Branding */
    @font-face {{
        font-family: 'WonderfulBranding';
        src: url(data:font/ttf;base64,{wonderful_base64}) format('truetype');
        font-size: 60px;
        font-weight: normal;
        font-style: normal;
    }}

    /* Fonte Cormorant Garamond para h2 e h3 */
    h2.fade-in, h3.fade-in {{
        font-family: 'Cormorant Garamond', serif !important;
        letter-spacing: 0.3em;
        line-height: 1.4;
        font-size: 20px;
        font-weight: 90;
        text-align: center;
        margin: 0;
        padding: 0;
    }}

    /* Aplicar Wonderful Branding ao h1 */
    h1.fade-in {{
        font-family: 'WonderfulBranding', serif !important;
        text-align: center;
        font-size: 50px;
        font-weight: 100;
    }}

    </style>
""", unsafe_allow_html=True)


# Títulos
st.markdown("""
    <h1 class="fade-in"></h1>
    <h1 class="fade-in">Lidia e Erick</h1>
    <h3 class="fade-in">CONTAGEM REGRESSIVA PARA O NOSSO SIM!</h3>
""", unsafe_allow_html=True)

# --------------------------------------
# Seção: Contagem regressiva
# --------------------------------------

import streamlit as st
from datetime import datetime
import time

st.set_page_config(layout="wide")
st.markdown("""
<style>

/* Estilo dos valores (números) */
[data-testid="stMetricValue"] > div {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 25px !important;
    letter-spacing: 0.3em !important;
    color: #2e2e2e !important;
}

/* Estilo dos labels (Dias, Horas, Minutos, Segundos) */
[data-testid="stMetricLabel"] > div {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 5px !important;
    font-weight: 90;
    line-height: 1.4;
    letter-spacing: 0.3em;
    color: #4a4a4a !important;
    text-transform: none !important;
}

</style>
""", unsafe_allow_html=True)

# Local onde o contador será atualizado
counter_placeholder = st.empty()

wedding_datetime = datetime(2026, 5, 1, 14)

# Loop que atualiza apenas o contador
while True:
    now = datetime.now()
    diff = wedding_datetime - now

    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Reescreve só este bloco — o resto da página fica intacto
    with counter_placeholder.container():

        # ESPAÇAMENTO LATERAL PARA CENTRALIZAR
        left, center, right = st.columns([1, 2, 1])

        with center:
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("DIAS", days)
            c2.metric("HORAS", hours)
            c3.metric("MINUTOS", minutes)
            c4.metric("SEGUNDOS", seconds)

    time.sleep(1)