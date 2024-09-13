from flask import Flask,request,jsonify
from Biseccion import biseccion
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/biseccion",methods=['POST'])
def hello_world():
    datos = request.get_json()
    xi = datos.get('Xi')
    xs = datos.get('Xs')