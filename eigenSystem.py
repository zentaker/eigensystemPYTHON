# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:22:25 2021

@author: Alejandro
"""

import matplotlib.pyplot as plt
import numpy as np

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

eigenfunction=[]
eigenfunctionxlist=[]
eigenenergies=[]


E=0
dE=0.01
dx=a*0.001

counter=1

#numero de niveles
nmax=5

while counter<=nmax:
    psi=1
    
    while abs(psi)>0.001:
        E=E+dE
        psi=0
        dpsi=1
        x=0
        xlist=[]
        psilist=[]

        while x<=a:
            ddpsi=2*m/h**2*(V-E)*psi
            dpsi=dpsi+ddpsi*dx
            psi=psi+dpsi*dx
            x=x+dx
            xlist.append(x)
            psilist.append(psi)
            
    eigenfunction.append([psilist])
    eigenfunctionxlist.append([xlist])
    eigenenergies.append(E)
    counter=counter+1
    E=E*1.1

counter=1
while counter<=nmax:
    plt.plot(xlist, eigenfunction[counter-1][0])
    counter=counter+1
    