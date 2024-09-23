import pandas as pd
import numpy as np
import sympy as sp
import math
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

def Newton(Fun, Tol, Niter, X0):
    fn=[]
    xn=[]
    E=[]
    N=[]
    x=X0
    f=eval(Fun)
    y = sp.Symbol('x')
    df= str(sp.diff(Fun,y))
    derivada= eval(df)
    x=X0
    c=0
    Error=100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error>Tol and f!=0 and derivada!=0  and c<Niter:
        x=x-f/derivada
        derivada = eval(df)
        f=eval(Fun)
        fn.append(f)
        xn.append(x)
        c=c+1
        Error=abs(xn[c]-xn[c-1])
        N.append(c)
        E.append(Error)
    if f==0:
        s=x
        print(s,"es raiz de f(x)")
    elif Error<Tol:
        s=x
        print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
        print("N",N)
        print("xn",xn)
        print("fn",fn)
        print("Error",E)
    else:
        s=x
        print("Fracaso en ",Niter, " iteraciones ") 


if __name__ == '__main__':
    print(Newton("(x**3)-(2*x)+1", 0.0001, 100, -1.5))


