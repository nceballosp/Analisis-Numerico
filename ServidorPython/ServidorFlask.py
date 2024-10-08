from flask import Flask,request,jsonify
from Biseccion import biseccion
from Secante import secante
from ReglaFalsa import ReglaFalsa
from PuntoFijo import PuntoFijo
from Newton import Newton
from NewtonRaicesMultiples1 import RaicesMultiples1
from NewtonRaicesMultiples2 import RaicesMultiples2

from RelajacionSOR import SOR
from Jacobi import MatJacobi

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
    resultado = secante(float(X0),float(X1),float(tol),float(Niter),func,ErrorType)
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
    resultado = ReglaFalsa(float(Xi),float(Xf),float(tol),float(Niter),func,ErrorType)
    return jsonify(resultado)

@app.route("/Punto-Fijo", methods=['POST'])
def FijoPunto():
    X0= request.form.get('X0')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    g = request.form.get('g')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = PuntoFijo(func,float(tol),float(Niter),float(X0),g,ErrorType)
    return jsonify(resultado)

@app.route("/Newton", methods=['POST'])
def tonnew():
    X0= request.form.get('X0')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    df = request.form.get('df')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = Newton(func,df,float(tol),float(Niter),float(X0),ErrorType)
    return jsonify(resultado)

@app.route("/Raices-Multiples-1", methods=['POST'])
def multiplesraices1():
    X0= request.form.get('X0')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    m = request.form.get('m')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = RaicesMultiples1(func,float(tol),float(Niter),float(X0),m,ErrorType)
    return jsonify(resultado)

@app.route("/Raices-Multiples-2", methods=['POST'])
def multiplesraices2():
    X0= request.form.get('X0')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    decimales = find_round_n(float(tol),ErrorType)
    resultado = RaicesMultiples2(func,float(tol),float(Niter),float(X0),ErrorType)
    return jsonify(resultado)

@app.route("/SOR", methods=['POST'])
def Sorrelajacion():
    x0= request.form.get('X0')
    A = request.form.get('A')
    b = request.form.get('b')
    w = request.form.get('w')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    # Convertir a lista y asegurarte de que 'tol' y 'Niter' sean del tipo correcto
    decimales = find_round_n(float(tol), ErrorType)
    resultado = SOR(np.array(eval(x0)), np.array(eval(A)), np.array(eval(b)), float(w), float(tol), int(Niter), ErrorType)
    # Convertir el resultado a una lista si es un ndarray
    if isinstance(resultado, np.ndarray):
        resultado = resultado.tolist() 
    return jsonify(resultado)

@app.route("/GaussSeidel", methods=['POST'])
def SeidelGauss():
    x0= request.form.get('X0')
    A = request.form.get('A')
    b = request.form.get('b')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    w = 1
    # Convertir a lista y asegurarte de que 'tol' y 'Niter' sean del tipo correcto
    decimales = find_round_n(float(tol), ErrorType)
    resultado = SOR(np.array(eval(x0)), np.array(eval(A)), np.array(eval(b)), float(w), float(tol), int(Niter), ErrorType)
    # Convertir el resultado a una lista si es un ndarray
    if isinstance(resultado, np.ndarray):
        resultado = resultado.tolist()  
    return jsonify(resultado)

@app.route("/Jacobi", methods=['POST'])
def JacobiMat():
    x0= request.form.get('X0')
    A = request.form.get('A')
    b = request.form.get('b')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    ErrorType = request.form.get('ErrorType')
    # Convertir a lista y asegurarte de que 'tol' y 'Niter' sean del tipo correcto
    decimales = find_round_n(float(tol), ErrorType)
    resultado = MatJacobi(np.array(eval(x0)), np.array(eval(A)), np.array(eval(b)), float(tol), int(Niter), ErrorType)
    # Convertir el resultado a una lista si es un ndarray
    if isinstance(resultado, np.ndarray):
        resultado = resultado.tolist()  
    return jsonify(resultado)


if __name__ == '__main__':
    app.run()
