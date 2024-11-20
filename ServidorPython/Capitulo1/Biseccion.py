import pandas as pd
import numpy as np
from SimpleWriting import *
#import wdb
#wdb.set_trace()

def biseccion(Xi,Xs,Tol,Niter,Fun,ErrorType):
    fm=[]
    E=[]
    xn=[]
    N = []
    x=Xi
    fi=eval(Fun)
    x=Xs
    fs=eval(Fun)
    

    if fi==0:
        s=Xi
        E=0
        state = 'Exact'
        tabla = [(0,s,fi,E)]
        return {'state':state,'tabla':tabla,'sol':s}
    elif fs==0:
        s=Xs
        E=0
        state = 'Exact'
        tabla = [(0,s,fs,E)]
        return {'state':state,'tabla':tabla,'sol':s}
    elif fs*fi<0:
        c=0
        N.append(c)
        Xm=(Xi+Xs)/2
        x=Xm  
        fe=eval(Fun)
        fm.append(fe)
        E.append(100)
        while E[c]>Tol and fe!=0 and c<Niter:
            if fi*fe<0:
                Xs=Xm
                xn.append(Xs)
                x=Xs
                fs=eval(Fun)
            else:
                Xi=Xm
                xn.append(Xi)
                x=Xi
                fi=eval(Fun)
            Xa=Xm
            Xm=(Xi+Xs)/2
            x=Xm 
            fe=eval(Fun)
            fm.append(fe)
            if ErrorType == 'Abs':
                Error=abs(Xm-Xa)
                E.append(Error)
            elif ErrorType == 'Rel':
                Error = abs((Xm-Xa)/Xm)
                E.append(Error)
            c=c+1
            N.append(c)
        if fe==0:
            sol=x
            state='Exact'
            tabla = zip(N,xn,fm,E)
            return {'state':state,'sol':sol,'tabla':tabla}
            # Solucion exacta
        elif Error<Tol:
                sol=x
                state = 'Aprox'
                tabla = list(zip(N,xn,fm,E))
                return{'state':state,'tabla':tabla,'sol':sol}
        else:
            # Fallado
            s=x
            state='Failed'
            return {'state':state,'Niter':Niter}
    else:
        # Invalido
        state='Invalid'
        return state
if __name__ == '__main__':
    print("X0:")
    Xi = float(input())
    print("X1:")
    Xs = float(input())
    print("Tol:")
    Tol = float(input())
    print("Niter:")
    Niter = float(input())
    print("Function:")
    Fun = input()
    print("Tipo de error:")
    ErrorType = input()
    print(biseccion(Xi,Xs,Tol,Niter,Fun,ErrorType))