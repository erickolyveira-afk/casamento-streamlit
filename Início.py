import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64
from pathlib import Path
import random
import base64

# ======================================================
# CONFIGURAÇÃO DA PÁGINA (SEMPRE PRIMEIRO)
# ======================================================
st.set_page_config(
    page_title="Nosso Casamento",
    page_icon="💍",
    layout="wide"
)

# ======================================================
# MÚSICA
# ======================================================

def spotify_player():
    st.markdown("""
    <style>
    iframe.spotify {
        filter: brightness(0.9) contrast(1.05);
        border-radius: 14px;
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)

    st.components.v1.html(
        """
        <iframe
            class="spotify"
            src="https://open.spotify.com/embed/playlist/3Wv0Wq2DorrZHzpV1eYU3Y"
            width="100%"
            height="80"
            frameborder="0"
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
        </iframe>
        """,
        height=90
    )

spotify_player()

# ======================================================
# AUTO REFRESH (1 segundo) — SEM LOOP
# ======================================================
st_autorefresh(interval=1000, key="contador")

# ======================================================
# CSS GLOBAL + SIDEBAR (FORÇANDO MODO CLARO)
# ======================================================
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

/* ======================================================
   METRICS (DESKTOP)
====================================================== */

div[data-testid="stMetric"] {
    text-align: center !important;
    width: fit-content !important;
    margin: 0 auto 18px auto !important;
}

[data-testid="stMetricValue"] > div {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 26px !important;
    letter-spacing: 0.2em !important;
    color: #2e2e2e !important;
}

[data-testid="stMetricLabel"] > div {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 11px !important;
    letter-spacing: 0.2em !important;
    color: #4a4a4a !important;
}

/* Remove espaçamento interno das colunas */
div[data-testid="column"] {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* ======================================================
   RESPONSIVO
====================================================== */

.desktop-only {
    display: block;
}

.mobile-only {
    display: none;
}

/* MOBILE */
@media (max-width: 768px) {

    .desktop-only {
        display: none;
    }

    .mobile-only {
        display: block;
        text-align: center;
    }

    .mobile-countdown {
        display: flex;
        justify-content: center;
        gap: 18px;
        font-family: 'Cormorant Garamond', serif;
    }

    .mobile-box {
        min-width: 60px;
    }

    .mobile-number {
        font-size: 22px;
        letter-spacing: 0.15em;
    }

    .mobile-label {
        font-size: 9px;
        letter-spacing: 0.2em;
        opacity: 0.7;
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
    desktop_img="images/layout/Floripa 311223 (5).jpg",
    mobile_img="images/layout/Floripa 311223.jpg"
)

# ======================================================
# FONTE WONDERFUL BRANDING
# ======================================================
font_path = Path("assets/fonts/WonderfulBranding.ttf")
with open(font_path, "rb") as f:
    font_base64 = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
<style>
@font-face {{
    font-family: 'WonderfulBranding';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}

@keyframes fadeUp {{
    from {{
        opacity: 0;
        transform: translateY(25px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.fade-in {{
    animation: fadeUp 1.8s ease-out forwards;
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
# TÍTULOS (APENAS MARKDOWN — SAFE PARA SAFARI)
# ======================================================
st.markdown(
    """
<h1 class="fade-in">Lidia e Erick</h1>
<h3 class="fade-in">CONTAGEM REGRESSIVA 
<br>PARA O NOSSO SIM!</h3>
""",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ======================================================
# CONTADOR
# ======================================================
wedding_datetime = datetime(2026, 5, 1, 14, 30)
now = datetime.now()
diff = wedding_datetime - now

days = diff.days
hours, remainder = divmod(diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# ================= DESKTOP =================
st.markdown('<div class="desktop-only">', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns([1, 1, 1, 1], gap="small")

c1.metric("DIAS", days)
c2.metric("HORAS", hours)
c3.metric("MINUTOS", minutes)
c4.metric("SEGUNDOS", seconds)

st.markdown('</div>', unsafe_allow_html=True)