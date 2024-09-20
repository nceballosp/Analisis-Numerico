import pandas as pd
import numpy as np
from SimpleWriting import *
#import wdb
#wdb.set_trace()

def secante(X0,X1,Tol,Niter,Fun):
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
        Error=abs(xn[c+1]-xn[c])
        N.append(c)
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


if __name__ == '__main__':
    print("X0:")
    X0 = float(input())
    print("X1:")
    X1 = float(input())
    print("Tol:")
    Tol = float(input())
    print("Niter:")
    Niter = float(input())
    print("Function:")
    Fun = input()
    print(secante(X0,X1,Tol,Niter,Fun))