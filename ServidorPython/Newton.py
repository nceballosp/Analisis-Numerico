import pandas as pd
import numpy as np
import sympy as sp
import math
from SimpleWriting import *
#import wdb
#wdb.set_trace()

# print("X0:")
# X0 = float(input())
# print("Tol:")
# Tol = float(input())
# print("Niter:")
# Niter = float(input())
# print("Function:")
# Fun = input()
# print("derivate Function df:")
# df = input()

def Newton(Fun, df,Tol, Niter, X0, ErrorType):
    fn=[]
    xn=[]
    E=[]
    N=[]
    x=X0
    f=eval(Fun)
    # x = sp.Symbol('x')
    # df= str(sp.diff(Fun,x).doit())
    df = str(df)
    derivada= eval(df)
    x=X0
    c=0
    Error=100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error>Tol and f!=0 and derivada!=0  and c<Niter:
        x=x-(f/derivada)
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
    print(Newton("-e(-x)+x*(-1-x)+x**(2/3)-1",'((3*x*(e(-x)))+(6*(x**2))-(2*(x**(2/3)))-(3*x))/(3*x)', 5e-6, 1000, 0.623,'Abs'))


