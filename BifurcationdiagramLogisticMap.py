#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 8 16:27:44 2021

@author: David Armenteros Soto
"""
"""
1.4 SISTEMAS DINÁMICOS DISCRETOS NO LINEALES
    1.4.2 EL MAPA LOGÍSTICO, DIAGRAMA DE BIFURCACIÓN Y CONSTANTE DE FEIGENBAUM
    
bifurcationdiagramLogisticMap.py es un programa que sirve de apoyo a la sección 1.4.2. Su finalidad es representar
la función logística según distintos parámetros de mu y  calcular las iteraciones del mapa 
a partir de un valor inicial x0. Esa información quedará reflejada mediante la representación 
de un diagrama de bifurcación o diagrama de Feigenbaum. Trás su ejecución, obtendremos imágenes 
que nos serán de gran utilidad para estudiar el comportamiento del sistema, conocer sus puntos periódicos, 
analizar la estabilidad, observar fenómenos caóticos,...
"""
import numpy as np
import matplotlib.pyplot as plt

def logistic(mu,x):
    """
    Definición de la función logística.
    
    Parámetros
    ----------
    mu : Parámetro mu de la función logística mu  \in [0,4].  
    x : Parámetro x de la función logística x \in [0,1] .
        
    Returns
    -------
    Valor de la función logística. 
    """
    return mu*x*(1.0-x)

def plotLogistic(mu):
    """
    Representación de la función logística
    
    Parámetros
    ----------
    mu : Parámetro mu de la función logística mu  \in [0,4].  
    """
    
    ejex=np.linspace(0,1, 50)
    plt.plot(ejex, mu*ejex*(1.0-ejex),'k-')
    plt.xlabel('x')
    plt.ylabel('f(x) logística')
    plt.show()
    
    
def plotLogisticIterations(mu,x0,n):
    """
    Cálculo de las iteraciones de la función logística a partir de un valor inicial
    
    Parámetros
    ----------
    mu : Parámetro mu de la función logística mu \in [0,4]. 
    x0 : Valor inicial x0 \in [0,1].
    n : Número de iteraciones
    """ 
    
    ejex = np.array([])
    ejey = np.array([])
    
    for i in range(1,n):
        x=x0
        for j in range(i):
            x=logistic(mu,x)
        ejex = np.append(ejex, i)
        ejey =np.append(ejey,x)

    plt.plot(ejex, ejey,'k-')
        
    plt.xlabel('n')
    plt.ylabel('f^n(x)')
    plt.show()
     

def bifDiagramLogistic(a,b,x0):
    """
    Diagrama de bifurcación del mapa logístico
    
    Parámetros
    ----------
    a: extremo inferior del intervalo [a,b] \subset [0,4]
    b: extremo superior del intervalo [a,b] \subset [0,4]
    x0 : Valor inicial x0 \in [0,1].
    """ 
    
    #Particionamos el intervalo [a,b] donde se mueve el valor de mu
    mu=np.arange(a,b,0.0001)
    #Número de iteraciones sin salida
    iteraciones=1500
    #Número de iteraciones para dibujar
    ultimas=100
    
    for i in range(iteraciones+ultimas):
        x0=logistic(mu,x0)
        if i>=iteraciones:
            plt.plot(mu,x0,color='black',markersize=0.1)
          
    plt.xlabel('\N{GREEK SMALL LETTER MU}')
    plt.ylabel('Xn')
    plt.show()

#Representación de la función logística
plotLogistic(3.5)


#Diagrama de bifurcación 
bifDiagramLogistic(2, 4, 0.2)
bifDiagramLogistic(0, 4, 1/2)
bifDiagramLogistic(0, 4, 0.9)
bifDiagramLogistic(2.5, 4, 0.5)

#Representación de las iteraciones de la función logística dependiendo del valor de mu
plotLogisticIterations(1/2,1/2,100)
plotLogisticIterations(2,1/2,100)
plotLogisticIterations(3.2,1/2,100)
plotLogisticIterations(3.50,1/2,100)
plotLogisticIterations(3.7,1/2,100)
plotLogisticIterations(3.9,1/2,100)
