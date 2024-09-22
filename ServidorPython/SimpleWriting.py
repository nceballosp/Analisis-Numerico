import math 
import numpy as np
def e(expresion):
    return math.exp(expresion)
def ln(expresion):
    return math.log(expresion)
def find_round_n(flt:float,ErrorType):
    decimal_count = 0
    flt = str(flt)
    if 'e' in flt:
        temp = flt.split('e')
        decimal_count = -int(temp[1])
    elif '.' in flt:
        temp = flt.split('.')
        decimal_count = -int(len(temp[1]))
    return decimal_count
if __name__ == '__main__':
    x = float(0.04e-5) # dc:6 cs:7 if n <=5 then dc:n-1 and cs:n
    y = float(0.07e-5) # dc:5  cs: 6 if n > 5 then dc:n-2 and cs:n-1
    z = float(0.7e-5) # dc:4 cs:5
    w = float(99999999999e-21) # dc: 5 cs:6
    print(x)
    print(y)
    print(z)
    print(w)