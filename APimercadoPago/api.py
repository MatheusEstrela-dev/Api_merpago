import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("TEST-7565279843969963-060218-ba530d1bd8a2858ffddcfe8791241ffb-179313123")

    payment_data = {
        "itens": [
            { "id": "1","title": "Sapato","quantity": 1, "currency_id": "BRL", "unit_price":19.99 },   
        ],
        "back_urls": {
            "success": "http://http://127.0.0.1:8000/compracerta.html",
            "pending": "http://http://127.0.0.1:8000/compraerrada.html",
            "failure": "http://http://127.0.0.1:8000/compraerrada.html"
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento



# init_point 

# http://www.mercadopago.com.br/checkout/v1/redirect?pref_id=144516549-286a4d448-23fb-44c5-b568-19d576d047ba