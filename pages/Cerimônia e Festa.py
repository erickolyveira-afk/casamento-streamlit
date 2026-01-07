import streamlit as st
from pathlib import Path

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
    font-size: 20px !important;
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
import base64

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

# Use o nome da sua imagem local aqui:
add_bg_from_local("images/layout/Casa-170.jpg")

st.title("Cerimônia e Festa")

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

    <b>Data:</b> 01/05/2026  
    <b>Horário:</b> 14h30  
    <b>Local:</b> R. das Seringueiras, 170 - Balneario Praia do Pernambuco, Guarujá - SP, 11444-340  
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

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
        font-size: 45px !important;
        font-weight: 100 !important;
        letter-spacing: 0.05em !important;
        text-align: center !important;
    }}

    h2, h3, h4, h5, h6 {{
        font-family: 'WonderfulBranding', serif !important;
        font-size: 20px !important;
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

    /* ==============================
       ARREDONDAR MAPA FOLIUM — COMPATÍVEL COM TODAS AS VERSÕES
       ============================== */

    /* Versions novas com stFolium */
    .stFolium, .stFolium > div, .stFolium iframe {{
        border-radius: 20px !important;
        overflow: hidden !important;
    }}

    /* Versões antigas (classe folium-map) */
    div.folium-map, div.folium-map iframe {{
        border-radius: 20px !important;
        overflow: hidden !important;
    }}

    /* Backup universal */
    .stApp iframe[src*="leaflet"], 
    .stApp iframe[src*="folium"] {{
        border-radius: 20px !important;
        overflow: hidden !important;
    }}

</style>
""", unsafe_allow_html=True)


# ==============================
# MAPA
# ==============================
lat, lon = -23.9609949, -46.1835808

m = folium.Map(
    location=[lat, lon],
    zoom_start=16,
    tiles="https://cartodb-basemaps-a.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png",
    attr="© CARTO"
)

icon = folium.Icon(color="pink", icon="heart", prefix="fa")

folium.Marker(
    [lat, lon],
    popup="Local",
    icon=icon
).add_to(m)

col = st.columns([1])[0]
with col:
    st_folium(m, height=200, width=None)

st.markdown(
    """
    <div class="texto-cerimonia">
    <h3 style="text-align:center;">Cerimônia</h3>

    Nossa celebração começa às <b>14h30</b>, na <b>Casa 170</b>, no Guarujá. Pedimos que cheguem com <b>15 minutinhos de antecedência</b> para aproveitarmos tudo juntos.
  
    O traje sugerido é <b>esporte fino</b>. Como a cerimônia será <b>ao ar livre</b>, vale levar um casaquinho caso esfrie ou protetor solar se o sol estiver forte.

    Para vivermos esse momento de um jeito ainda mais especial, optamos por uma <b>cerimônia desconectada</b>: sem fotos ou gravações. Queremos vocês inteiros com a gente, curtindo cada segundo ao vivo.

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .texto-festa {
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
    
        .texto-festa > div {
            margin-bottom: 1rem;
        }

        .texto-festa > div:last-child {
            margin-bottom: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="texto-festa">
    <h3 style="text-align:center;">Recepção e Festa</h3>

    <b>O local da festa será no mesmo endereço da cerimônia</b>, então ninguém precisará se preocupar com deslocamentos ou transporte entre os eventos.

    A recepção acontece logo após a cerimônia e, em seguida, inicia a festa com <b>duração prevista de 4 horas</b>. Por isso, aproveitem cada minuto com a gente!

    Preparamos um <b>cardápio variado</b>, um <b>bar de drinks completo</b> e, claro, <b>open bar de cerveja</b> para deixar a noite ainda mais especial.

    </div>
    """,
    unsafe_allow_html=True
)

