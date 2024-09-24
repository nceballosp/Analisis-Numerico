import pandas as pd
import numpy as np
import sympy as sp
import math

def RaicesMultiples2(Fun, Tol, Niter, X0,ErrorType):
    fn=[]
    xn=[]
    E=[]
    N=[]
    x=X0
    f=eval(Fun)
    y = sp.Symbol('x')
    df= str(sp.diff(Fun,y))
    dff = str(sp.diff(df,y))
    derivada= eval(df)
    derivada2 = eval(dff)
    x=X0
    c=0
    Error=100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error>Tol and f!=0 and derivada!=0  and c<Niter:
        x=x-((f*derivada)/((derivada**2)-(f*derivada2)))
        derivada = eval(df)
        f=eval(Fun)
        fn.append(f)
        xn.append(x)
        c=c+1
        if ErrorType=='Abs':
            Error=abs(xn[c]-xn[c-1])
            E.append(Error)
        elif ErrorType == 'Rel':
            Error = abs((xn[c]-xn[c-1])/xn[c])
            E.append(Error)
        N.append(c)
    if f==0:
        s=x
        state = 'Exact'
        tabla = list(zip(N,xn,fn,E))
        return {'state':state,'tabla':tabla}
    elif Error<Tol:
        s=x
        state = 'Aprox'
        tabla = list(zip(N,xn,fn,E))
        return {'state':state,'tabla':tabla}
    else:
        s=x
        state = 'Failed'
        return {'state':state, 'Niter':Niter}

if __name__ == '__main__':
    (RaicesMultiples2("(x**3)-(2*x)+1", 0.0001, 100, -1.5))
