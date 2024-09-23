from flask import Flask,request,jsonify
from Biseccion import biseccion
from Secante import secante
from ReglaFalsa import ReglaFalsa
from flask_cors import CORS
from SimpleWriting import *
app = Flask(__name__)
CORS(app)

@app.route("/Biseccion",methods=['POST'])
def seccionbi():
    Xi = request.form.get('Xi')
    Xf = request.form.get('Xf')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = biseccion(float(Xi),float(Xf),float(tol),float(Niter),func,ErrorType,decimales)
    return jsonify(resultado)

@app.route("/Secante", methods=['POST'])
def cantese():
    X0= request.form.get('X0')
    X1= request.form.get('X1')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = secante(float(X0),float(X1),float(tol),float(Niter),func)
    return jsonify(resultado)

@app.route("/Regla-Falsa", methods=['POST'])
def FalsaRegla():
    Xi = request.form.get('Xi')
    Xf = request.form.get('Xf')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = ReglaFalsa(float(Xi),float(Xf),float(tol),float(Niter),func,decimales)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run()