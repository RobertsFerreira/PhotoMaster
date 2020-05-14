import json
from flask import Flask, g, request, jsonify, Response, send_file
import jsonpickle
import cv2
from filtrosServe import *

app = Flask(__name__)


@app.route("/enviarfoto", methods=['POST'])
def enviarfoto():
    # requisação que se faz ao App.
    r = request
    # pega o arraydata da img e seu metódo de codificação.
    nparr = np.fromstring(r.data, np.uint8)
    # leitura dela com o metodo de codificação dela.
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Aviso de recepção.
    response = {
        f'message': 'image received. size={img.shape[1]}x{img.shape[0]}'}
    # transforma a string em json.
    response_pickled = jsonpickle.encode(response)
    filename = 'D:/Program Files (x86)/Repositorio/PhotoMaster/Original.png'
    cv2.imwrite(filename, img)
    changefiltro('negativo', filename)
    changefiltro('logaritmo', filename)
    changefiltro('logInverso', filename)
    changefiltro('prewitt', filename)

    print('foi')

    return Response(response=response_pickled,
                    status=200, mimetype="application/json",)


@app.route('/receberfoto/<filtro>')
def receberfoto(filtro):
    g.filtro = filtro
    caminhofoto = ""
    if filtro == "negativo":
        caminhofoto = "d:\\Program Files (x86)\\Repositorio\\PhotoMaster\\ImagemNegativada.png"
    elif filtro == "logaritmo":
        caminhofoto = "d:\\Program Files (x86)\\Repositorio\\PhotoMaster\\ImagemComLogaritmo.png"
    elif filtro == "logInverso":
        caminhofoto = "d:\\Program Files (x86)\\Repositorio\\PhotoMaster\\ImagemComlogInverso.png"
    elif filtro == "original":
        caminhofoto = "d:\\Program Files (x86)\\Repositorio\\PhotoMaster\\Original.png"
    elif filtro == "prewitt":
        caminhofoto = "d:\\Program Files (x86)\\Repositorio\\PhotoMaster\\ImagemcomPrewitt.png"

    return send_file(caminhofoto, mimetype='image/png')


@app.route('/teste')
def teste():
    return '[{"status": "ok"}]'


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
