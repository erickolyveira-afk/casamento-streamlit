import mercadopago
import os

sdk = mercadopago.SDK(
    "APP_USR-5926755074577430-122615-8a4a967289f3c75def678f6d52bd5fe7-228841284"
)

def criar_pagamento_cartao(total, nome):
    preference_data = {
        "items": [
            {
                "title": f"Presente de casamento – {nome}",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(total),
            }
        ],
        "payment_methods": {
            "installments": 6
        },
        "back_urls": {
            "success": "https://example.com/success",
            "failure": "https://example.com/failure",
            "pending": "https://example.com/pendente",
        },
        "auto_return": "approved",
    }

    preference = sdk.preference().create(preference_data)
    return preference["response"]["init_point"]