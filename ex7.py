# Não consegui passar os dados com a curl, coloquei header e body manualmente no Thunderclient.

from flask import Flask, request
app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def soma():
    if request.get_json(silent=True):
        valores = request.json
        x = valores["x"]
        y = valores["y"]
        soma = (x+y)
        return (f'"resultado":"{soma}"')



if __name__ == '__main__':
    app.run(debug=True)