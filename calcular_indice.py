# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:05:52 2020

@author: -
"""

clase=1
stotal= 0
uv1=0
while clase == 1:
    nota= float(input("Nota: "))
    uv= float(input("UV= "))
    stotal= (nota*uv)+stotal
    uv1=uv+uv1
    clase = int(input("¿Una clase más? (sí=1 / no=0): "))
    if clase==0:
        break
    elif clase==1:
        clase=1
print(uv1, stotal)
total= (stotal/uv1)
print(total)