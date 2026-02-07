import mercadopago

sdk = mercadopago.SDK(
    "APP_USR-5926755074577430-122615-8a4a967289f3c75def678f6d52bd5fe7-228841284"
)

def criar_pagamento_cartao(total, nome, checkout_id):
    preference_data = {
        "items": [
            {
                "title": f"Presente de casamento – {nome}",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(total),
            }
        ],

        # ✅ Parcelamento
        "payment_methods": {
            "installments": 12,
            "excluded_payment_types": [
                {"id": "pix"},
                {"id": "boleto"}
            ]
        },

        # 🔁 URLs COM ESTADO
        "back_urls": {
            "success": f"https://casamento-lidia-e-erick.streamlit.app/Lista_de_Presentes?checkout_id={checkout_id}&status=sucesso",
            "failure": f"https://casamento-lidia-e-erick.streamlit.app/Lista_de_Presentes?checkout_id={checkout_id}&status=erro",
            "pending": f"https://casamento-lidia-e-erick.streamlit.app/Lista_de_Presentes?checkout_id={checkout_id}&status=pendente",
        },

        "auto_return": "approved"
    }

    preference = sdk.preference().create(preference_data)
    return preference["response"]["init_point"]