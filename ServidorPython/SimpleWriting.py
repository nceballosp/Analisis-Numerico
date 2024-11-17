import math 
import numpy as np
def exp(expresion):
    return math.exp(expresion)
def ln(expresion):
    return math.log(expresion)
def find_round_n(flt:float,ErrorType):
    decimal_count = 0
    number = 0
    flt = str(flt)  
    if 'e' in flt:
        temp = flt.split('e')
        decimal_count = -int(temp[1])
        number = float(temp[0])
        if ErrorType == 'Abs':
            if number <=5:
                decimal_count-= 1
            elif number > 5:
                decimal_count -= 2
        elif ErrorType == 'Rel':
            if number <=5:
                pass
            elif number > 5:
                decimal_count -=1    
    elif '.' in flt:
        #revisar
        temp = flt.split('.')
        decimal_count = int(len(temp[1]))
        if ErrorType == 'Abs':
            pass

        
    return decimal_count
if __name__ == '__main__':
    x = float(0.04e-5) # dc:6 cs:7 if n <=5 then dc:n-1 and cs:n
    y = float(0.07e-5) # dc:5  cs: 6 if n > 5 then dc:n-2 and cs:n-1
    z = float(0.7e-5) # dc:4 cs:5
    w = float(99999999999e-21) # dc: 5 cs:6
    i = float(9.2)
    print(find_round_n(x,'Abs'))
    print(find_round_n(x,'Rel'))
    print(find_round_n(y,'Abs'))
    print(find_round_n(y,'Rel'))
    print(find_round_n(z,'Abs'))
    print(find_round_n(z,'Rel'))
    print(find_round_n(w,'Abs'))
    print(find_round_n(w,'Rel'))
    print(find_round_n(i,'Abs'))
    print(find_round_n(i,'Rel'))