# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:26:36 2021

@author: Alejandro
"""

import matplotlib.pyplot as plt
import numpy as np
# contante
h=1
# massa del electron
m=1
#definir elpotencial
a=1
#potencial dentro de la caja 
V=0
#ecuacion de la onda en la pocicion incial
psi=0
#definir la derivada tiene que ser diferente de 0
dpsi=1
#comenzamos en x = 0
x=0
#realizamos uin incremento 1000 pasos hasta estar al otro lado de la caja
dx=a*0.001

#lista para nuestros valores de x
xlist=[]
#valores de la funcion de onda
psilist=[]

#energy
E=123.1
while x<=a:
    ddpsi=2*m/h**2*(V-E)*psi
    dpsi=dpsi+ddpsi*dx
    psi=psi+dpsi*dx
    x=x+dx
    xlist.append(x)
    psilist.append(psi)
    plt.plot(xlist,psilist)