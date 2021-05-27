from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola mundo"


@app.route("/post/<post_id>", methods=["GET"])
def lala(post_id):
    return "El id del post es: " + post_id


@app.route("/post/<post_id>", methods=["POST"])
def lili(post_id):
    return "El id del post es: " + post_id


@app.route("/example-request/<data_request>", methods=["GET", "POST"])
def lele(data_request):
    if request.method == "GET":
        return "El dato enviado desde la url es: " + data_request
    else:
        return "Este es otro metodo y no get"


@app.route("/lolo", methods=["POST", "GET"])
def lolo():
    # abort(404)
    # return redirect(url_for("lala", post_id=2))
    # print(request.form['nombre'])
    # print(request.form['apellido'])
    # return render_template("lele.html")
    return {"username": "Chanchito Feliz", "email": "chanchito@feliz.com"}


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", message="Hello World")
