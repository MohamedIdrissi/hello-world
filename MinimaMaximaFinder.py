#Find local minima/maxima numerically 
import numpy as np

def fy(x):

    return #function

def minmaxf(f):
    x = list(np.arange(-10,10,0.0001))
    d = []
    cp = []
    for xi in x:
        d.append(f(xi))
    
    for i in range(len(d)-2):
        if d[i+2] < d[i+1] and d[i+1] > d[i]:
            cp.append(["Local Max",round(x[i+1],3),round(x[i],3)])
        if d[i+2] > d[i+1] and d[i+1] < d[i]:
            cp.append(["Local Min",round(x[i+1],3),round(x[i],3)])
    return (cp)