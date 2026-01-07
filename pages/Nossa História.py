import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

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
add_bg_from_local("images/layout/PEDIDO.jpg")

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
        font-size: 40px !important;   /* 👈 AQUI VOCÊ AJUSTA */
        font-weight: 100 !important;
        letter-spacing: 0.05em !important;
        text-align: center !important;
        color: #FBFBF8 !important;
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

st.title("Nossa História")

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
    <div>De uma apresentação escolar a encontros inusitados e aleatórios pelas ruas e trens, com o passar do tempo, muitas vezes refletimos sobre nossa história. Por isso, preferimos acreditar que todos esses encontros foram obra do acaso, que simplesmente tinham de acontecer.</div>
    <div>Desde o período em que éramos apenas amigos, quando nos tornamos confidentes um do outro, até o momento em que iniciamos nosso relacionamento, a vida sempre pareceu sorrir quando estávamos juntos, seja nas salas de cinema ou simplesmente caminhando por aí. Com o tempo, foi interessante perceber que não se tratava da situação em si, mas sim da companhia.</div>
    <div>Foi dessa forma que passamos a nos encontrar quase todos os dias, seja para compromissos definidos ou para situações mais simples e banais, como levar um brigadeiro até o portão dela apenas para ter uma desculpa para vê-la.</div>
    <div>Ao longo desses anos, não faltaram desafios, dificuldades e situações que nos forçaram a crescer e amadurecer, tanto como casal quanto individualmente. É bonito perceber como todas essas experiências alimentaram nossa relação e a transformaram em algo melhor para nós dois. Assim, agradecemos não apenas pelos bons momentos, mas também pelos difíceis, que nos ensinaram que nosso parceiro sempre estará ao nosso lado para cuidar da gente.</div>
    <div>Então, até hoje nós agradecemos muito àquela apresentação de faculdade, aquele sinal vermelho e aquele trem parado. Agradecemos a todas as situações que nos conduziram aos nossos encontros e, hoje: “a gente se escolhe todo dia e escolheríamos em mais um milhão de vidas”.</div>
    <div>Quando é para acontecer, tem dia, lugar e tem hora 🤍
    </div>
    """,
    unsafe_allow_html=True
)


