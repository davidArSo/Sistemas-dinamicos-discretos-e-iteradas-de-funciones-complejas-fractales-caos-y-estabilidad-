#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:38:45 2021

@author: David Armenteros Soto
"""
"""
2 INTRODUCCIÓN A LA TEORÍA DEL CAOS 
    2.4 EXPONENTE DE LYAPUNOV
    
LyapunovExponent.py es un programa que sirve de apoyo a la sección 2.4. Su finalidad es representar el 
exponente de Lyapunov junto con el diagrama de bifurcación del mapa logístico. Trás su ejecución, se 
obtienen ambas representaciones y el valor del exponente para determinados
mu. La salida del programa ayuda a entender el comportamiento del mapa logístico
y sirve para corroborar la teoría de la sección 2.4.
"""

import numpy as np
import matplotlib.pyplot as plt
import math 
import statistics


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


def logisticDerivative(mu,x):
    """
    Definición de la derivada de la función logística.
    
    Parámetros
    ----------
    mu : Parámetro mu de la función logística mu  \in [0,4].  
    x : Parámetro x de la función logística x \in [0,1] .
        
    Returns
    -------
    Valor de la derivada de la función logística. 
    """
    return mu*(1.0-2*x)
    


def LyapunovExponentLogistic(a,b,x0):
    """
    Exponente de Lyapunov para la función logística
    
    Parámetros
    ----------
    a: extremo inferior del intervalo [a,b] \subset [0,4]
    b: extremo superior del intervalo [a,b] \subset [0,4]
    x0 : Valor inicial x0 \in [0,1]. 
    """
   
    #Particionamos el intervalo [a,b] donde se mueve el valor de mu
    mu=np.arange(a,b,0.01)
    #Número de iteraciones sin salida
    iteraciones=1500
    #Número de iteraciones para dibujar
    ultimas=100
    
    #Guardamos el valor de las derivadas 
    derivadas=[]
    #Guardamos el valor de la media de las derivadas 
    media=[]
    
    print ("Para a: ", a, " b: ", b, " x0: ", x0, "Se tiene que: ")
    
    
    for pos in range (mu.size):
        x=x0
        derivadas=[]
        
        for i in range (iteraciones):

            x=logistic(mu[pos],x)
            aux1=logisticDerivative(mu[pos],x)
            if(aux1 != 0):
                aux=math.log(abs(aux1))
                derivadas=np.append(derivadas,aux)
        if(  len(derivadas) != 0):
            media=np.append(media,statistics.mean(derivadas))
        else:
            media=np.append(media,0)
        
        aprox=round(mu[pos],2)
        
        if aprox == 0.5:
            print ("Si mu: ", 0.5, " el exponente de Lyapunov es: ", media[len(media)-1])
        if aprox == 1:
            print ("Si mu: ", 1, " el exponente de Lyapunov es: ", media[len(media)-1])
        if aprox == 2.5:
            print ("Si mu: ", 2.5, " el exponente de Lyapunov es: ", media[len(media)-1])
        if aprox == 3:
            print ("Si mu: ", 3, " el exponente de Lyapunov es: ", media[len(media)-1])
        if aprox == 3.5:
            print ("Si mu: ", 3.5, " el exponente de Lyapunov es: ", media[len(media)-1])
        if aprox == 3.6:
            print ("Si mu: ", 3.6, " el exponente de Lyapunov es: ", media[len(media)-1])
        if aprox == 3.97:
            print ("Si mu: ", 3.97, " el exponente de Lyapunov es: ", media[len(media)-1])

    fig=plt.figure()
    ax=fig.add_subplot()
    
    for i in range(iteraciones+ultimas):
        x0=logistic(mu,x0)
        if i>=iteraciones:
            
            if(i==iteraciones):    
                plt.plot(mu,x0,color='red',markersize=0.1, label='Diagrama bifurcación')
            else:
                plt.plot(mu,x0,color='red',markersize=0.1)
                
            
    
    ejex=np.linspace(a,b,1000)
    fnula=[0]*1000
    ax.plot(ejex,fnula,'black')
    ax.plot(mu,media,'b',label='Exponente de Lyapunov')
    ax.set_ylim(-1,1)
    ax.set_xlabel('\N{GREEK SMALL LETTER MU}')
    ax.grid('on')
    ax.legend(loc='best')

#Representación del diagrama de bifurcación y el exponente de Lyapunov
LyapunovExponentLogistic(2,4,0.1)
LyapunovExponentLogistic(0,4,0.6)
LyapunovExponentLogistic(3,4,0.6)
LyapunovExponentLogistic(1,3.8,0.47)
