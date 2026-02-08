import streamlit as st
import base64
import csv
import smtplib
import streamlit.components.v1 as components
from email.message import EmailMessage
from datetime import datetime
from pathlib import Path
from data.presentes import presentes
from utils.pix import gerar_pix_payload, gerar_qr
from utils.credito import criar_pagamento_cartao
from utils.checkout import carregar_estado_checkout, salvar_estado_checkout

query_params = st.query_params

checkout_id = query_params.get("checkout_id")
status = query_params.get("status")

if checkout_id:
    dados = carregar_estado_checkout(checkout_id)

    st.session_state["nome"] = dados.get("nome")
    st.session_state["mensagem"] = dados.get("mensagem")
    st.session_state["carrinho"] = dados.get("carrinho", [])

    if status == "sucesso":
        st.session_state["pagina"] = "credito_sucesso"

    elif status == "erro":
        st.session_state["pagina"] = "credito_erro"

    elif status == "pendente":
        st.session_state["pagina"] = "credito_pendente"

    st.experimental_set_query_params()
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

h2, h3, h4, h5, h6,
p, label {{
    font-family: 'Cormorant Garamond', serif !important;
}}

/* Label pequeno do filtro */
[data-testid="stSelectbox"] > label {{
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 10px !important;
}}

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

# ==============================
# ESTADO
# ==============================
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = []

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "lista"

# ==============================
# CSS DOS CARDS
# ==============================
st.markdown("""
<style>
.card {
    background: white;
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    text-align: center;
    margin-bottom: 24px;
    transition: transform 0.2s ease;
}
.card:hover {
    transform: translateY(-6px);
}
.card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 12px;
}
.card-title {
    font-size: 20px;
    margin-top: 12px;
}
.card-desc {
    font-size: 14px;
    color: #666;
    margin: 8px 0;
}
.card-price {
    font-size: 18px;
    font-weight: 600;
    margin: 10px 0;
}
.cart-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# FUNÇÃO SALVAR MENSAGEM DE PAGAMENTO
# ==============================
def salvar_mensagem(nome, mensagem, carrinho, total):
    arquivo = Path("mensagens_presentes.csv")
    arquivo_existe = arquivo.exists()

    with open(arquivo, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not arquivo_existe:
            writer.writerow([
                "Data",
                "Nome",
                "Mensagem",
                "Presentes",
                "Total"
            ])

        presentes = ", ".join([item["nome"] for item in carrinho])

        writer.writerow([
            datetime.now().strftime("%d/%m/%Y %H:%M"),
            nome,
            mensagem,
            presentes,
            f"R$ {total:.2f}"
        ])

# ==============================
# FUNÇÃO SALVAR MENSAGEM DE PAGAMENTO
# ==============================
def enviar_email(nome, mensagem, carrinho, total):
    EMAIL_REMETENTE = "erick.olyveira@gmail.com"
    SENHA_APP = "nmmm xihc uazt gusr"
    EMAIL_DESTINO = "pic-pics@outlook.com"

    presentes = "\n".join([f"- {item['nome']} (R$ {item['preco']:.2f})" for item in carrinho])

    corpo = f"""
NOVO PRESENTE RECEBIDO

Nome:
{nome}

Mensagem:
{mensagem}

Presentes:
{presentes}

Total:
R$ {total:.2f}
"""

    msg = EmailMessage()
    msg["Subject"] = "Novo presente recebido!"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINO
    msg.set_content(corpo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_REMETENTE, SENHA_APP)
        smtp.send_message(msg)

# ==============================
# FUNÇÃO AUXILIAR
# ==============================
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==============================
# SIDEBAR — CARRINHO
# ==============================
st.sidebar.markdown("<h2>🛒 Meu Carrinho</h2>", unsafe_allow_html=True)

if st.session_state["carrinho"]:
    total_sidebar = 0

    for idx, item in enumerate(st.session_state["carrinho"]):
        st.sidebar.markdown(
            f"""
            <div class="cart-item">
                <b>{item['nome']}</b>
                <span>R$ {item['preco']:.2f}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.sidebar.button("Remover", key=f"remove_{idx}",
                            use_container_width=True):
            st.session_state["carrinho"].pop(idx)
            st.rerun()

        st.sidebar.markdown("---")
        total_sidebar += item["preco"]

    st.sidebar.markdown(f"### Total: R$ {total_sidebar:.2f}")

    if st.sidebar.button("Finalizar compra",
                        use_container_width=True):
        st.session_state["pagina"] = "checkout"
        st.rerun()
else:
    st.sidebar.write("Seu carrinho está vazio 🛍️")

# ==============================
# TELA — LISTA
# ==============================
if st.session_state["pagina"] == "lista":
    st.title("Lista de Presentes")

    # 🔽 FILTRO DE ORDENAÇÃO (NOVO)
    col_filtro, _ = st.columns([1, 5])
    with col_filtro:
        ordenar_por = st.selectbox(
            "Ordenar por",
            ["Padrão", "Menor preço", "Maior preço"]
        )

    # 🔁 ORDENAÇÃO (NOVO)
    presentes_ordenados = presentes.copy()

    if ordenar_por == "Menor preço":
        presentes_ordenados = sorted(
            presentes,
            key=lambda x: (x["id"] == 20, x["preco"])
        )

    elif ordenar_por == "Maior preço":
        presentes_ordenados = sorted(
            presentes,
            key=lambda x: (x["id"] == 20, -x["preco"])
        )

    cols = st.columns(3)

    for idx, presente in enumerate(presentes_ordenados):
        with cols[idx % 3]:
            img_b64 = img_to_base64(presente["imagem"])

            st.markdown(f"""
            <div class="card">
                <img src="data:image/jpeg;base64,{img_b64}">
                <div class="card-title">{presente["nome"]}</div>
                <div class="card-desc">{presente["descricao"]}</div>
                <div class="card-price">
                    {"Valor livre" if presente["id"] == 20 else f"R$ {presente['preco']:.2f}"}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "🎁 Presentear",
                key=f"btn_{presente['id']}",
                use_container_width=True
            ):
                st.session_state["carrinho"].append(presente)
                st.toast(f"{presente['nome']} adicionado ao carrinho 🎉")
                st.rerun()
                
# ==============================
# TELA 2 — CHECKOUT
# ==============================
if st.session_state["pagina"] == "checkout":
    st.title("Finalizar Presente")

    total = sum(item["preco"] for item in st.session_state["carrinho"])

    for idx, item in enumerate(st.session_state["carrinho"]):

        # 🎁 Presente Misterioso
        if item["id"] == 20:
            valor = st.number_input(
                "Quanto você gostaria de presentear? 💝",
                min_value=0.00,
                step=1.00,
                value=float(item["preco"]),
                key=f"misterioso_{idx}"
            )

            st.session_state["carrinho"][idx]["preco"] = valor
            st.write(f"🎁 {item['nome']} — R$ {valor:.2f}")

        else:
            st.write(f"🎁 {item['nome']} — R$ {item['preco']:.2f}")

    st.markdown(f"### Total: R$ {total:.2f}")

    nome = st.text_input("Seu nome")
    mensagem = st.text_area("Mensagem para os noivos 💌", max_chars=300)

    st.session_state["nome"] = nome
    st.session_state["mensagem"] = mensagem

    col1, col2 = st.columns(2)

    # ✅ PIX — confirmação manual
    with col1:
        if st.button("💠 Pagar com PIX", use_container_width=True):
            salvar_mensagem(
                st.session_state["nome"],
                st.session_state["mensagem"],
                st.session_state["carrinho"],
                total
            )

            enviar_email(
                st.session_state["nome"],
                st.session_state["mensagem"],
                st.session_state["carrinho"],
                total
            )

            st.session_state["pagina"] = "pix"
            st.rerun()

    # ✅ CARTÃO — só redireciona
    with col2:
        if st.button("💳 Pagar com Cartão", use_container_width=True):
            st.session_state["pagina"] = "credito"
            st.rerun()

    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state["pagina"] = "lista"
        st.rerun()

# ==============================
# TELA 3 — PAGAMENTO PIX
# ==============================
if st.session_state["pagina"] == "pix":
    st.title("💠 Pagamento via PIX")

    total = sum(item["preco"] for item in st.session_state["carrinho"])

    payload = gerar_pix_payload(
        chave="erick.oliveira@usp.br",
        nome="ERICK DE OLIVEIRA COSTA",
        cidade="MAUA",
        valor=total
    )

    st.subheader("PIX Copia e Cola")
    st.code(payload)
    st.image(gerar_qr(payload), width=260)

    st.info("Após realizar o pagamento, clique no botão abaixo")

    if st.button("Já realizei o pagamento ✅", use_container_width=True):
        salvar_mensagem(
            st.session_state["nome"],
            st.session_state["mensagem"],
            st.session_state["carrinho"],
            total
        )

        enviar_email(
            st.session_state["nome"],
            st.session_state["mensagem"],
            st.session_state["carrinho"],
            total
        )

        st.success("Pagamento registrado! Muito obrigado pelo carinho!!")

        # opcional: limpar carrinho
        st.session_state["carrinho"] = []

    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state["pagina"] = "checkout"
        st.rerun()

# ==============================
# TELA 4 — PAGAMENTO CARTÃO
# ==============================

st.markdown("""
<div style="
    background:#FDF5E6;
    border-radius:12px;
    padding:14px;
    text-align:center;
    font-family:'Cormorant Garamond', serif;
    font-size:18px;
    color:#4a4a4a;
    margin-bottom:15px;
">
💳 <b>Cartão de crédito</b><br>
Parcelamento disponível conforme análise do Mercado Pago e do banco emissor.
</div>
""", unsafe_allow_html=True)

if st.session_state["pagina"] == "credito":
    st.title("💳 Pagamento com Cartão de Crédito")

    total = sum(item["preco"] for item in st.session_state["carrinho"])
    st.write(f"💰 Total: R$ {total:.2f}")

    if st.button("🔐 Pagar com cartão", use_container_width=True):
        checkout_id = salvar_estado_checkout()

        link = criar_pagamento_cartao(
            total,
            st.session_state.get("nome", "Convidado"),
            checkout_id=checkout_id
        )

        st.session_state["redirect_url"] = link

    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state["pagina"] = "checkout"
        st.rerun()

if st.session_state.get("redirect_url"):
    components.html(
        f"""
        <script>
            window.location.href = "{st.session_state['redirect_url']}";
        </script>
        """,
        height=0
    )

# ==============================
# RETORNO — CARTÃO APROVADO
# ==============================
if st.session_state["pagina"] == "credito_sucesso":
    st.title("💖 Pagamento confirmado!")

    total = sum(item["preco"] for item in st.session_state["carrinho"])

    salvar_mensagem(
        st.session_state["nome"],
        st.session_state["mensagem"],
        st.session_state["carrinho"],
        total
    )

    enviar_email(
        st.session_state["nome"],
        st.session_state["mensagem"],
        st.session_state["carrinho"],
        total
    )

    st.success("Muito obrigado pelo carinho! 💐")

    st.session_state["carrinho"] = []

    if st.button("Voltar para a lista"):
        st.session_state["pagina"] = "lista"
        st.rerun()


# ==============================
# RETORNO — CARTÃO PENDENTE
# ==============================
if st.session_state["pagina"] == "credito_pendente":
    st.title("⏳ Pagamento pendente")

    st.warning(
        "Seu pagamento ainda está em análise pelo Mercado Pago. "
        "Assim que for aprovado, ele será confirmado automaticamente."
    )

    if st.button("Voltar"):
        st.session_state["pagina"] = "lista"
        st.rerun()


# ==============================
# RETORNO — CARTÃO COM ERRO
# ==============================
if st.session_state["pagina"] == "credito_erro":
    st.title("❌ Pagamento não concluído")

    st.error(
        "O pagamento não foi aprovado. "
        "Você pode tentar novamente ou escolher outra forma de pagamento."
    )

    if st.button("Tentar novamente"):
        st.session_state["pagina"] = "checkout"
        st.rerun()
