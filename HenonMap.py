#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:46:50 2021

@author: David Armenteros Soto
"""
"""
1.4 SISTEMAS DINÁMICOS DISCRETOS NO LINEALES
    1.4.4 MAPA DE HÉNON
    
henonMap.py es un programa que sirve de apoyo a a la sección 1.4.4. Su finalidad es representar la función 
de Hénon según distintos parámetros de alfa y beta.
"""

import numpy as np
import matplotlib.pyplot as plt

def henon(alfa,beta,x,y):
    """
    Definición de la función de Hénon.
    
    Parámetros
    ----------
    alfa : Parámetro alfa de la función de Hénon, alfa > 0.
    beta : Parámetro beta de la función de Hénon, |beta|<1.
    x: coordenada x del punto (x,y) del mapa de Hénon.
    y: coordenada y del punto (x,y) del mapa de Hénon.
        
    Returns
    -------
    Valor de la función de Hénon. 
    """
    
    return 1+y-alfa*x*x, beta*x


def henonMap(alfa,beta,x0,y0,n):
    """
    Cálculo de la órbita de un punto del mapa de Hénon. 
    
    Parámetros
    ----------
    alfa : Parámetro alfa de la función de Hénon, alfa > 0.
    beta : Parámetro beta de la función de Hénon, |beta|<1.
    x0: coordenada x del valor inicial (x0,y0) del mapa de Hénon.
    y0: coordenada y del valor inicial (x0,y0) del mapa de Hénon.
    n: número de iteraciones
    """ 

    x= np.array([])
    y= np.array([])
    x= np.append(x, x0)
    y= np.append(y, y0)
    print("X0,Y0 : (" ,x0," , " ,y0, " )")
    
    
    for i in range (1,n):
        x0, y0 =henon(alfa,beta,x0,y0)
        x= np.append(x, x0)
        y= np.append(y ,y0)
        print("Iteración ", i ," : (" ,x0," , " ,y0, " )")
        
 
     #La opcion '^' es para pintar SOLO los puntos
    plt.plot(x,y,'^', color='black',markersize=0.7 )
    plt.show()
   
#Función de Hénon para alfa=1,2, beta=0.4 y (x0,y0)=(0.1,0)
henonMap(1.2, 0.4, 0.1, 0, 1000)
