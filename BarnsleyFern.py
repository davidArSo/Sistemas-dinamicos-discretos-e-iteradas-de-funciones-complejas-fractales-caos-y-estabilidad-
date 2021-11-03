#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:23:06 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.3 Sistema de funciones iteradas (SFI)
        4.3.1 Algoritmos para la obtención del fractal asociado a un SFI
            4.3.1.2 SFI aleatorio y el juego del caos
                Ejemplo 4.11 El helecho de Barnsley 
        
BarnsleyFern.py es un programa que sirve de apoyo al ejemplo 4.11. Su finalidad es construir el helecho de Barnsley
a partir de su sistema de funciones iteradas (SFI) con el algoritmo aleatorio.
"""

import matplotlib.pyplot as plt
from  random import randint

#Definición de las contracciones
def f1(x,y):
    return (0.,0.16*y)

def f2(x,y):
    return (0.85*x+0.04*y, -0.04*x+0.85*y+1.6)

def f3(x,y):
    return (0.2*x-0.26*y,0.23*x+0.22*y+1.6)

def f4(x,y):
    return (-0.15*x + 0.28*y , 0.26*x + 0.24*y + 0.44)
     

def BarnsleyFernRandom(num_puntos):
    """
    Representa el helecho de barnsley con el algoritmo aleatorio

    Parámetros
    ----------
    num_puntos: número de puntos con los que se genera el helecho de Barnsley
    """
    
    x, y = 0, 0
    x_p = []
    y_p = []
    
    for i in range (num_puntos):
        #Generamos un entero aleatorio
        random=randint(1,100)
        
        #Si el número es 1, aplicamos f1 (probabilidad 0.01)
        if random == 1:
            x,y =f1(x,y)
            x_p.append(x)
            y_p.append(y)
            
        #Si el número está entre 2 y 86, aplicamos f2 (propabilidad 0.85)
        elif random>=2 and random<=86:
            x,y =f2(x,y)
            x_p.append(x)
            y_p.append(y)
        
        #Si el número está entre 87 y 93, aplicamos f3 (propabilidad 0.07)
        elif random >= 87 and random <=93:
            x,y =f3(x,y)
            x_p.append(x)
            y_p.append(y)
        
        #Si el número está entre 94 y 100, aplicamos f4 (propabilidad 0.07)
        elif random >=94 and random<=100:
            x,y =f4(x,y)
            x_p.append(x)
            y_p.append(y)
            

    plt.axis('off')
    plt.scatter(x_p, y_p,s=0.1, edgecolors='green')
    #plt.savefig('BarnsleyFern.png')
    plt.show()
            
            
BarnsleyFernRandom(1000)   
BarnsleyFernRandom(10000)  
BarnsleyFernRandom(100000)   
     