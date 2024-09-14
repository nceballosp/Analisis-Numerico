from flask import Flask,request,jsonify
from Biseccion import biseccion
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/Biseccion",methods=['POST'])
def hello_world():
    Xi = request.form.get('Xi')
    Xf = request.form.get('Xf')
    func = request.form.get('func')
    tol = request.form.get('Tol')
    Niter = request.form.get('Niter')
    resultado = biseccion(float(Xi),float(Xf),float(tol),float(Niter),func)
    if resultado['state'] == 'Exact':
        return jsonify(resultado)
    elif resultado['state'] == 'Aprox':
        return jsonify(resultado)
    return '202'
if __name__ == '__main__':
    app.run()