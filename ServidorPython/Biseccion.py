import pandas as pd
import numpy as np
from SimpleWriting import *
#import wdb
#wdb.set_trace()

def biseccion(Xi,Xs,Tol,Niter,Fun):
    fm=[]
    E=[]
    x=Xi
    fi=eval(Fun)
    x=Xs
    fs=eval(Fun)

    if fi==0:
        s=Xi
        E=0
        print(Xi, "es raiz de f(x)")
    elif fs==0:
        s=Xs
        E=0
        print(Xs, "es raiz de f(x)")
    elif fs*fi<0:
        c=0
        Xm=(Xi+Xs)/2
        x=Xm  
        fe=eval(Fun)
        fm.append(fe)
        E.append(100)
        while E[c]>Tol and fe!=0 and c<Niter:
            if fi*fe<0:
                Xs=Xm
                x=Xs
                fs=eval(Fun)
            else:
                Xi=Xm
                x=Xi
                fs=eval(Fun)
            Xa=Xm
            Xm=(Xi+Xs)/2
            x=Xm 
            fe=eval(Fun)
            fm.append(fe)
            Error=abs(Xm-Xa)
            E.append(Error)
            c=c+1
        if fe==0:
            sol=x
            state='Exact'
            return {'state':state,'sol':sol}
            # print(s,"es raiz de f(x)")
            # Solucion exacta
        elif Error<Tol:
                sol=x
                state = 'Aprox'
                return{'state':state,'sol':sol,'Tol':Tol,'fm':fm,'E':E}
                # print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
                # print("Fm",fm)
                # print("Error",E)
            # Criterio Optimista
        else:
            # Fallado
            s=x
            state='Failed'
            return {'state':state,'Niter':Niter}
            print("Fracaso en ",Niter, " iteraciones ") 
    else:
        # Invalido
        state='Invalid'
        return state
        print("El intervalo es inadecuado")
