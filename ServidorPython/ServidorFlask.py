from flask import Flask,request,jsonify
from Biseccion import biseccion
from flask_cors import CORS
from SimpleWriting import *
app = Flask(__name__)
CORS(app)

@app.route("/Biseccion",methods=['POST'])
def hello_world():
    Xi = request.form.get('Xi')
    Xf = request.form.get('Xf')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = biseccion(float(Xi),float(Xf),float(tol),float(Niter),func,ErrorType,decimales)
    return jsonify(resultado)
if __name__ == '__main__':
    app.run()