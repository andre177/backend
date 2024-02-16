from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
@app.route('/consulta_cep', methods=['GET'])
def cep():
    cep = request.args['cep']
    request_url = "https://viacep.com.br/ws/" + cep + "/json/"
    dados_cep = requests.get(request_url)
    response = jsonify(dados_cep.json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/cotacao', methods=['GET'])
def cotacao():
    moeda1 = request.args['moeda1']
    moeda2 = request.args['moeda2']
    request_url = "https://economia.awesomeapi.com.br/last/" + moeda1 + "-" + moeda2
    cotacao = requests.get(request_url)
    response = jsonify(cotacao.json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/health', methods=['GET'])
def healthcheck():
    response = jsonify({'status': 'ok'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run(host='0.0.0.0', port=5000)