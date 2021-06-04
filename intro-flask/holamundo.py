from types import TracebackType
from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="tareas_electrica"
)

# Aqui cambiamos la forma en que nos va a entregar los datos
# en vez de entregar una lista de tuplas
# ahora nos entrega una lista de diccionarios
cursor = mydb.cursor(dictionary=True)


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
    cursor.execute("select * from technician")
    tecnicos = cursor.fetchall()
    # abort(404)
    # return redirect(url_for("lala", post_id=2))
    # print(request.form['nombre'])
    # print(request.form['apellido'])
    # return render_template("lele.html")
    # return {"username": "Chanchito Feliz", "email": "chanchito@feliz.com"}
    return render_template("lele.html", tecnicos=tecnicos)


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", message="Hello World")


@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cargo = request.form["cargo"]
        turno = request.form["turno"]
        query = "insert into technician(nombre, cargo_t, turno) values(%s, %s,%s)"
        values = (nombre, cargo, turno)
        cursor.execute(query, values)
        mydb.commit()

        # redireccionamos al usuario a lolo
        return redirect(url_for("lolo"))
    return render_template("crear.html")
