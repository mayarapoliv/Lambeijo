from srv.view import View
from srv.database import LambeijosDB

from flask import Flask, request, render_template, request, redirect, url_for  # Importa a biblioteca

app = Flask(__name__, template_folder="template")  # Inicializa a aplicação

view = View()

@app.route("/", methods=['GET', 'POST'])
def auth():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        id  = view.auth_validation(usuario, senha)
        if id:
            return redirect(url_for("client", id=id))
        else:
            return render_template("index.html", erro="Usuário ou senha inválidos")


@app.route("/client/<int:id>")  # Cria uma rota
def client(id):
    view.get_all_cliente_from_id(id)
    return render_template("pag2Cliente.html")


@app.route("/table/")  # Cria uma rota
def table():
    id = request.form['id']
    database = LambeijosDB()
    dados = database.ler_mensagens()

    return render_template("tabela.html",dados)

@app.route("/boletim1/")  # Cria uma rota
def boletim1():
    id = request.form['id']
    database = LambeijosDB()
    dados = database.ler_mensagens()
    return render_template("Boletim1.html",dados)


@app.route("/boletim2/")  # Cria uma rota
def boletim2():
    id = request.form['id']
    database = LambeijosDB()
    dados = database.ler_mensagens()
    return render_template("Boletim2.html",dados)

if __name__ == "__main__":
    app.run(debug=True)  # Executa a aplicação

