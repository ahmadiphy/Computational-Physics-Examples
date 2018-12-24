#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:11:17 2018

@author: Ahmadi
"""
import matplotlib.pyplot as plt
import numpy as np

def f(y):
    return y

def calc_n(x0,xf,h):
    return (xf-x0)/h

def xp(x,h):
    return x+h

def yp(y,h):
    return y+h*f(y)

x0=0.
y0=1
h=0.01
xf=5.
x=[]
x.append(x0)
y=[]
y.append(y0)
for i in range(int(calc_n(x0,xf,h))):
    x.append(xp(x[i],h))
    y.append(yp(y[i],h))
    #print(x[i],y[i])  

plt.plot(x,y,linestyle="",marker="o",markersize=0.5)
xx = np.arange(x0, xf, 0.001)
plt.plot(xx,np.exp(xx),color='red')
plt.xlabel("x",fontsize=15)
plt.ylabel("exp(x)",fontsize=15)
plt.savefig("./myplot.eps",format="eps",dpi=2200)
plt.show
