from flask import Flask, jsonify
import os

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00},
    {"id": 2, "nome": "Mouse", "preco": 80.00},
    {"id": 3, "nome": "Teclado", "preco": 150.00}
]

@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "API de Produtos executando com Docker!"
    })

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.route("/configuracao")
def configuracao():
    return jsonify({
        "ambiente": os.getenv("AMBIENTE", "desenvolvimento")
    })

if __name__ == "__main__":
    porta = int(os.getenv("PORTA", 5000))
    app.run(host="0.0.0.0", port=porta)