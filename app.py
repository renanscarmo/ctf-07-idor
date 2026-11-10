import os
import secrets

from flask import Flask, abort, redirect, request, session

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)

USUARIOS = ["ana", "bruno", "carla"]

PEDIDOS = {
    1: {"dono": "ana", "item": "Camiseta", "valor": "49,90"},
    2: {"dono": "bruno", "item": "Caneca", "valor": "29,90"},
    3: {
        "dono": "carla",
        "item": "Vale-presente FLAG{idor_pedido_de_outra_pessoa}",
        "valor": "100,00",
    },
}

FORMULARIO = """
<h1>Loja do Renan</h1>
<form method="post">
  <input name="usuario" placeholder="ana, bruno ou carla">
  <button type="submit">Entrar</button>
</form>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        if usuario in USUARIOS:
            session["usuario"] = usuario
            return redirect("/meus-pedidos")
        return FORMULARIO + "<p>Usuario nao encontrado.</p>"
    return FORMULARIO


@app.route("/meus-pedidos")
def meus_pedidos():
    usuario = session.get("usuario")
    if not usuario:
        return redirect("/")
    links = ""
    for numero, pedido in PEDIDOS.items():
        if pedido["dono"] == usuario:
            links += f"<li><a href='/pedido/{numero}'>Pedido {numero}</a></li>"
    return f"<h1>Ola, {usuario}!</h1><ul>{links}</ul>"


@app.route("/pedido/<int:numero>")
def ver_pedido(numero):
    if not session.get("usuario"):
        return redirect("/")
    pedido = PEDIDOS.get(numero)
    if not pedido:
        abort(404)
    return f"<h1>Pedido {numero}</h1><p>{pedido['item']} - R$ {pedido['valor']}</p>"


if __name__ == "__main__":
    app.run()