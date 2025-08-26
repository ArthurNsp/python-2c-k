from models.produto_models import produto
from db import db
import json
from flask import make_response

def create_produto(produto_data):
    novo_produto = produto(
        modelo=produto_data['modelo'],
        marca=produto_data['marca'],
        ano=produto_data['ano']
    )

    db.session.add(novo_produto)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Notebook cadastrado com sucesso.',
            'produto': novo_produto.json()
        }, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response