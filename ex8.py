# Não consegui passar os dados com a curl, coloquei header e body manualmente no Thunderclient.

from flask import Flask, request
app = Flask(__name__)

numero = 0
numero = int(numero)

@app.route('/contador', methods=['GET'])
def contador_get():
        return (f'"numero":"{numero}"'),200


@app.route('/contador', methods=['POST'])
def contador_post():
    if request.get_json(silent=True):
        valores = request.json
        global numero
        numero = valores['numero']
        return (f'"numero":"{numero}"'),201


@app.route('/contador/incrementa', methods=['PUT'])
def contador_incrementa():
    global numero
    numero = int(numero) + 1
    return (f'"numero":"{numero}"'),202


@app.route('/contador', methods=['DELETE'])
def contador_delete():
    global numero
    numero = 0
    return (f'"numero":"{numero}"'),202



if __name__ == '__main__':
    app.run(debug=True)