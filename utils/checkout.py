import json
from uuid import uuid4
import streamlit as st
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def salvar_estado_checkout():
    checkout_id = str(uuid4())

    dados = {
        "nome": st.session_state.get("nome"),
        "mensagem": st.session_state.get("mensagem"),
        "carrinho": st.session_state.get("carrinho"),
    }

    with open(DATA_DIR / f"checkout_{checkout_id}.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False)

    return checkout_id


def carregar_estado_checkout(checkout_id):
    with open(DATA_DIR / f"checkout_{checkout_id}.json", "r", encoding="utf-8") as f:
        return json.load(f)