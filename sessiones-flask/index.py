from flask import Flask
from flask import make_response
from flask.globals import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    try:
        resp = make_response('Inicio de session correctamente')
        resp.set_cookie('mi_cookie', 'Otra super cookie')

        return resp
    except:
        return 'no pudo salir'

@app.route('/recupera', methods=['GET'])
def recupera():
    try:
        miCookie = request.cookies.get('mi_cookie')
        print(miCookie)
        return 'Recupera'
    except:
        return 'No recupera :('
