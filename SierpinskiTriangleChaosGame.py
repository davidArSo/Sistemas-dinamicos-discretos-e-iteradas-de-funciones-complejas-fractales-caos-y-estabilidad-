#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:03:58 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.3 Sistema de funciones iteradas (SFI)
        4.3.1 Algoritmos para la obtención del fractal asociado a un SFI
            4.3.1.2 SFI aleatorio y el juego del caos
                Ejemplo 4.12 El triángulo de Sierpinski aleatorio
        
SierpinskiTriangleChaosGame.py es un programa que sirve de apoyo al ejemplo 4.12.
Su finalidad es construir el triángulo de Sierpinski jugando al juego del caos.
"""

import matplotlib.pyplot as plt
import random as rand
import numpy as np

def Midpoint(u,v):
    """
    Calcula el punto medio 
    
    Parámetros
    ----------
    u: punto en el plano
    v: punto en el plano
    
    Returns
    -------
    Devuelve el punto medio
    """ 
    ux, uy = u
    vx, vy = v
    
    return (ux+vx)/2 , (uy+vy)/2 

def SierpinskiTriangleRandom(num_puntos, A, B, C ):
    """
    Representa el triángulo de Sierpinski con el juego del caos

    Parámetros
    ----------
    num_puntos: número de puntos con los que se genera el triángulo de Sierpinski
    A: vértice del triángulo incial
    B: vértice del triángulo inicial
    C: vértice del triángulo inicial
    """
    
    a1, a2 = A
    b1, b2 = B
    c1, c2 = C
    
    #Defino mi triángulo ABC
    trianguloABC=[(a1,a2), (b1,b2), (c1,c2)]
    
    #Inicializo el vector
    x_p = [0]*num_puntos
    y_p = [0]*num_puntos
    
    #Genero un punto aleatorio dentro del triángulo ABC
    u1=rand.random()
    u2=rand.random()

    if u1 + u2 > 1:
        u1=1-u1
        u2=1-u2
    
    x_p[0], y_p[0]= u1*(b1-a1) + u2*(b2-a2) , u1*(c1-a1) +u2*(c2-a2) 

    
    #Lanzo el "dado" y según el número añado el nuevo punto al vector
    for i in range (1,num_puntos):
        random=rand.randint(1,3)
        x_p[i], y_p[i] = Midpoint (trianguloABC[random-1], (x_p[i-1],y_p[i-1]))
    
    plt.axis('off')
    plt.scatter(x_p, y_p,s=0.1, edgecolors='black')
    #plt.savefig('SierpinskiTriangleRandom.png')
    plt.show()
        

SierpinskiTriangleRandom(1000, [0,0], [2,2*np.sqrt(3)],[4,0] )
SierpinskiTriangleRandom(10000, [0,0], [2,2*np.sqrt(3)],[4,0] )
SierpinskiTriangleRandom(100000, [0,0], [2,2*np.sqrt(3)],[4,0] )
  
     