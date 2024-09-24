import pandas as pd
import numpy as np
import math


def PuntoFijo(Fun, Tol, Niter, X0, g, ErrorType):
    fn=[]
    xn=[]
    E=[]
    N=[]
    x=X0
    f=eval(Fun)
    c=0
    Error=100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error>Tol and f!=0 and c<Niter:
        x=eval(g)
        fe=eval(Fun)
        fn.append(fe)
        xn.append(x)
        c=c+1
        N.append(c)
        if ErrorType == 'Abs':
                Error=abs(xn[c]-xn[c-1])
                E.append(Error)
        elif ErrorType == 'Rel':
            Error = abs((xn[c]-xn[c-1])/(xn[c]))
            E.append(Error)
    if fe==0:
        s=x
        state = 'Exact'
        tabla = list(zip(N,xn,fn,E))
        return {'state':state,'tabla':tabla,'sol':s}
    elif Error<Tol:
        s=x
        state = 'Aprox'
        tabla = list(zip(N,xn,fn,E))
        return {'state':state,'tabla':tabla,'sol':s}
    else:
        s=x
        state = 'Failed'
        return {'state':state,'message':f'Fracaso en {Niter} iteraciones'}



