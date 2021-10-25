#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 9 16:14:09 2021

@author: David Armenteros Soto
"""
"""
1.4 SISTEMAS DINÁMICOS DISCRETOS NO LINEALES
    1.4.3 MAPA DE GAUSS 

bifurcationdiagramGaussMap.py es un programa que sirve de apoyo a la sección 1.4.3 cuya finalidad es representar la función 
de Gauss según distintos parámetros de alfa y beta y  calcular las iteraciones del mapa 
a partir de un valor inicial x0. Esa información quedará reflejada mediante la representación 
de un diagrama de bifurcación. Trás su ejecución, obtendremos imágenes 
que nos serán de gran utilidad para  estudiar como se comporta el sistema dinámico discreto, conocer sus puntos periódicos, 
estabilidad, fenómenos caóticos,...
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def gauss(alfa,beta,x):
    """
    Definición de la función de Gauss.
    
    Parámetros
    ----------
    alfa : Parámetro alfa de la función de Gauss, alfa es una constante real.
    beta : Parámetro beta de la función de Gauss, beta es una constante real.
    x : Parámetro x de la función de Gauss x \in R .
        
    Returns
    -------
    Valor de la función de Gauss. 
    """
    return math.exp(-alfa*x*x)+beta

def plotGauss(alfa,beta):
    """
    Representación de la función de Gauss.
    
    Parámetros
    ----------
    alfa : Parámetro alfa de la función de Gauss, alfa es una constante real.
    beta : Parámetro beta de la función de Gauss, beta es una constante real.
    """

    ejex = np.array([])
    ejey = np.array([])
    ejex=np.linspace(-2,2, 50)
    for i in range (50):
        x=gauss(alfa, beta, ejex[i])
        ejey =np.append(ejey,x)

    plt.plot(ejex, ejey ,'k-')
    plt.xlabel('x')
    plt.ylabel('G(x) Gauss')
    plt.show()

def plotIntersectionGauss(alfa,beta):
    """
    Representación de la intersección del mapa de Gauss con la diagonal.
    
    Parámetros
    ----------
    alfa : Parámetro alfa de la función de Gauss, alfa es una constante real.
    beta : Parámetro beta de la función de Gauss, beta es una constante real.
    """

    ejex=np.linspace(-2,2, 20)
    plt.plot(ejex, ejex,'r-')
    plotGauss(alfa,beta)
    

def bifDiagramGaussMap(a,b,alfa,x0):
    """
    Diagrama de bifurcación del mapa de Gauss
    
    Parámetros
    ----------
    a: extremo inferior del intervalo [a,b] 
    b: extremo superior del intervalo [a,b] 
    alfa : Parámetro alfa de la función de Gauss, alfa es una constante real.
    x0 : Valor inicial x0 \in [0,1].
    """ 
    #Particionamos el intervalo [a,b] donde se mueve el valor de beta
    beta=np.linspace(a,b,500)
    #Número de iteraciones 
    iteraciones=50
   
    for i in beta:
        for j in range(iteraciones):
            x0=gauss(alfa,i,x0)
            plt.plot(i,x0,'^',color='black',markersize=0.1)
       
                
    plt.xlabel('\N{GREEK SMALL LETTER BETA}')
    plt.ylabel('Xn')
    plt.show()

#Representación de la función de Gauss
plotGauss(1,4)
plotGauss(4,1)


#Representación de la función de Gauss
plotIntersectionGauss(30,-1/2)
plotIntersectionGauss(4,1)
plotIntersectionGauss(13,-1/2)


#Diagrama de bifurcación
bifDiagramGaussMap(-1, 1, 8, 0)
bifDiagramGaussMap(-1, 1, 4, 0)
