#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 8 11:32:56 2021

@author: David Armenteros Soto
"""
"""
1.4 SISTEMAS DINÁMICOS DISCRETOS NO LINEALES
    1.4.1 MAPA TIENDA
    
tentMap.py es un programa que sirve de apoyo a la sección 1.4.1. Su finalidad es representar 
la función tienda según distintos parámetros de mu y calcular las iteraciones del mapa a partir 
de un valor inicial x0. Trás su ejecución, obtendremos imágenes que nos serán de gran
utilidad para analizar el comportamiento del sistema dinámico, observar sus puntos periódicos, estudiar
su estabilidad, ....  
"""

import numpy as np
import matplotlib.pyplot as plt

def T(mu,x): 
    """
    Definición de la función tienda T(X).
    
    Parámetros
    ----------
    mu : Parámetro mu de la función tienda mu \in [0,2].  
    x : Parámetro x de la función tienda x \in [0,1] .
        
    Returns
    -------
    Valor de la función tienda. 
    """
    
    if x>=0 and x<=1/2:
        return mu*x
    elif x>=1/2 and x<=1: 
        return mu*(1-x)
    

def T2(mu,x):
    """
    Definición de la segunda iterada de la función tienda T^2(X).
    
    Parámetros
    ----------
    mu : Parámetro mu de la función tienda mu \in [0,2].
    x : Parámetro x de la función tienda x \in [0,1] 
        
    Returns
    -------
    Valor de la segunda iterada de la función tienda. 
    """
    
    if x>=0 and x<=1/(2*mu):
        return mu*mu*x
    elif x>1/(2*mu) and x<=1/2: 
        return mu*(1-mu*x)
    elif x> 1/2 and x<=1-1/(2*mu): 
        return mu*(1-mu*(1-x))
    elif x>1-1/(2*mu) and x<=1: 
        return mu*mu*(1-x)
    
def plotT(mu):
    """
    Representación del mapa tienda
    
    Parámetros
    ----------
    mu : Parámetro mu de la función tienda mu \in [0,2]. 
    """
    
    ejex1=np.linspace(0,1/2, 100)
    ejex2=np.linspace(1/2,1, 100)
    plt.plot(ejex1, mu*ejex1,'k-')
    plt.plot(ejex2, mu*(1-ejex2),'k-')
    plt.xlabel('x')
    plt.ylabel('T(x)')
    plt.show()
    
def plotIntersectionT(mu):
    """
    Intersección del mapa tienda con la diagonal y=x
    
    Parámetros
    ----------
    mu : Parámetro mu de la función tienda mu \in [0,2]. 
    """ 
    plotT(mu)
    ejex=np.linspace(0,1, 20)
    plt.plot(ejex, ejex,'r-')
    
    

def plotIntersectionT2(mu):
    """
    Intersección de la segunda iterada del mapa tienda con la diagonal y=x
    
    Parámetros
    ----------
    mu : Parámetro mu de la función tienda mu \in [0,2]. 
    """ 
    
    ejex=np.linspace(0,1, 4)
    plt.plot(ejex, ejex,'r-')
    
    ejex1=np.linspace(0,1/(2*mu), 10)
    ejex2=np.linspace(1/(2*mu),1/2, 10)
    ejex3=np.linspace(1/2, 1-1/(2*mu), 10)
    ejex4=np.linspace(1-1/(2*mu),1, 10)
    
    plt.plot(ejex1,mu*mu*ejex1 ,'k-')
    plt.plot(ejex2,mu*(1-mu*ejex2) ,'k-')
    plt.plot(ejex3,mu*(1-mu*(1-ejex3)) ,'k-')
    plt.plot(ejex4,mu*mu*(1-ejex4),'k-')
    
    plt.xlabel('x')
    plt.ylabel('T^2(x)')
    plt.show()
    
def tentMap(mu,x0,n):
    """
    Cálculo y representación gráfica de la órbita de un punto del mapa tienda
    
    Parámetros
    ----------
    mu : Parámetro mu de la función tienda mu \in [0,2]. 
    x0 : Valor inicial x0 \in [0,1].
    n : Número de iteraciones
    """ 
    
    #Arrays para almacenar los puntos para representar la órbita
    inputs = np.array([])
    outputs = np.array([])
    
    #Primer punto (x0,0)
    inputs = np.append(inputs, x0)
    outputs = np.append(outputs, 0)
    
    print("X0:  ",x0)
    x=x0
    
    #Obtención de los puntos, como resultado de las iteraciones de T
    for i in range(1,n):
        inputs = np.append(inputs, x)
        inputs = np.append(inputs, x)
        outputs = np.append(outputs, x)
        x=T(mu,x)
        print("Iteración ", i ," :" ,x)
        outputs = np.append(outputs, x)
    
    #Obtenemos como resultados dos conjuntos de puntos:
    #    inputs  = { x0, x0,   x0,  T(x0), T(x0), ...}
    #    outputs = { 0,  x0, T(x0), T(x0), T^2(x0), ...}
        
        
    #Representamos los puntos en el plano (azul)
    plt.plot(inputs,outputs,'b-')
    
    #Gráfica de la función tienda y la recta y=x
    plotIntersectionT(mu)
    
    
     #La última opción de plot es para cambiar el color
     #Negro: Función tienda
     #Azul: Iteraciones
     #Rojo: Recta y=x
    

#Función tienda para mu= 1/2, 1, 3/2, 2
plotT(1/2)
plotT(1)
plotT(3/2)
plotT(2)

#Función tienda y diagonal para mu= 1/2, 1, 3/2
plotIntersectionT(1/2)
plotIntersectionT(1/2)
plotIntersectionT(1)
plotIntersectionT(3/2)

#Método gráfico para estudiar el comportamiento de la función tienda a partir 
#de un valor inicial x0
tentMap(0.5,1/4, 8)
tentMap(0.5, 1/2,  8)
tentMap( 0.5, 3/4, 8)
       
tentMap(2, 0.2, 100)
tentMap(2, 0.2001, 100)

tentMap( 1.5, 1/3, 50)
tentMap( 1.5, 6/13, 50)
 
#Función tienda T^2(x) para mu=2
plotIntersectionT2(2)
plotIntersectionT2(1.5)
