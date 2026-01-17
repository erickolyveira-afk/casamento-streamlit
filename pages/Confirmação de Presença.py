import streamlit as st
import base64
from pathlib import Path
import pandas as pd
from datetime import datetime

from google.oauth2.service_account import Credentials
import gspread


# ======================================================
# CONFIGURAÇÃO GOOGLE SHEETS
# ======================================================

SHEET_ID = "1khxlBw8EeznvAFuQhMUq-P5xFVAFjrV_4p04AcRkokI"

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

gc = gspread.authorize(credentials)
sheet = gc.open_by_key(SHEET_ID).sheet1


# ======================================================
# FUNÇÃO: LER PLANILHA
# ======================================================

def get_data():
    records = sheet.get_all_records()
    return pd.DataFrame(records)


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
    color: #4a4a4a !important;
    font-size: 18px !important;
    text-decoration: none !important;
}

[data-testid="stSidebar"] a:hover {
    color: #F5DEB3 !important;
}
</style>
""", unsafe_allow_html=True)


# ======================================================
# BLOQUEAR MODO ESCURO
# ======================================================

st.markdown("""
<style>
:root { color-scheme: light; }

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
        desktop = base64.b64encode(f.read()).decode()
    with open(mobile_img, "rb") as f:
        mobile = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{desktop}");
        background-size: cover;
        background-position: center;
    }}

    @media (max-width: 768px) {{
        .stApp {{
            background-image: url("data:image/jpeg;base64,{mobile}");
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


add_responsive_background(
    "images/layout/Floripa 311224.jpg",
    "images/layout/Floripa 311223.jpg"
)


# ======================================================
# FONTE WONDERFUL BRANDING
# ======================================================

font_path = Path("assets/fonts/WonderfulBranding.ttf")
font_base64 = base64.b64encode(font_path.read_bytes()).decode()

st.markdown(
    f"""
<style>
@font-face {{
    font-family: 'WonderfulBranding';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}

h1.fade-in {{
    font-family: 'WonderfulBranding', serif !important;
    font-size: 52px;
    text-align: center;
    font-weight: 100;
    margin-bottom: 10px;
}}

h3.fade-in {{
    font-family: 'Cormorant Garamond', serif !important;
    letter-spacing: 0.3em;
    text-align: center;
    font-weight: 300;
    margin-top: 0;
}}
</style>
""",
    unsafe_allow_html=True
)


# ======================================================
# TÍTULO
# ======================================================

st.markdown(
    """
    <h1 class="fade-in">Confirme aqui sua presença</h1>
    """,
    unsafe_allow_html=True
)


# ======================================================
# FORMULÁRIO
# ======================================================

nome = st.text_input("Seu nome completo:")

confirmacao = st.selectbox(
    "Você confirma presença?",
    ["Sim", "Não"]
)

if st.button("Enviar resposta"):

    df = get_data()

    if not nome.strip():
        st.error("Por favor, informe seu nome.")

    elif not df.empty and nome.strip().lower() in df["nome"].str.lower().values:
        st.error("⚠️ Este nome já foi registrado.")

    else:
        sheet.append_row([
            nome.strip(),
            confirmacao,
            datetime.now().strftime("%d/%m/%Y %H:%M")
        ])
        st.success("💛 Obrigado! Sua presença foi registrada com sucesso.")


# ======================================================
# CONTADOR AUTOMÁTICO
# ======================================================

st.markdown("---")

df = get_data()

if not df.empty:

    total = len(df)
    sim = len(df[df["confirmacao"] == "Sim"])
    nao = len(df[df["confirmacao"] == "Não"])

    c1, c2, c3 = st.columns(3)
    c1.metric("📋 Respostas", total)
    c2.metric("✅ Confirmados", sim)
    c3.metric("❌ Não irão", nao)


# ======================================================
# DASHBOARD DOS NOIVOS
# ======================================================

st.markdown("---")
st.subheader("Área dos Noivos 💍")

senha = st.text_input("Senha de acesso", type="password")

if senha == "lidiaeerick2026":

    st.success("Acesso liberado 💛")

    if not df.empty:
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Baixar lista de convidados",
            csv,
            "confirmados.csv",
            "text/csv"
        )