import pandas as pd
import numpy as np
from SimpleWriting import *
#import wdb
#wdb.set_trace()

def secante(X0,X1,Tol,Niter,Fun,ErrorType):
    fn=[]
    xn=[]
    E=[]
    N=[]
    x=X0
    f=eval(Fun)
    fn.append(f)
    x=X1
    f = eval(Fun)
    fn.append(f)
    c=0
    Error=100               
    xn.append(X0)
    xn.append(X1)
    E.append(Error)
    N.append(c)

    while Error>Tol and f!=0 and c<Niter:
        c=c+1
        x = xn[c] - (fn[c]*(xn[c]-xn[c-1])/(fn[c]-fn[c-1]))
        f=eval(Fun)
        fn.append(f)
        xn.append(x)
        N.append(c)
        if ErrorType == 'Abs':
                Error=abs(xn[c+1]-xn[c])
                E.append(Error)
        elif ErrorType == 'Rel':
            Error = abs((xn[c+1]-xn[c])/(xn[c+1]))
            E.append(Error)
    if f==0:
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


#if __name__ == '__main__':
  