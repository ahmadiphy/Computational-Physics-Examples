#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:44:28 2018

@author: classic
"""

import random

def fx(x):
    return x

xrange=10
yrange=10
n=10000
m=100
intValue=0#مقدار انتگرال 
for j in range(m):
    inF=0
    for i in range(n):
        r1=random.random()
        r2=random.random()
        x1=r1*xrange
        y1=r2*yrange
        if fx(x1)>y1:
            inF+=1
    intValue += 100*inF/n

print(intValue/m)