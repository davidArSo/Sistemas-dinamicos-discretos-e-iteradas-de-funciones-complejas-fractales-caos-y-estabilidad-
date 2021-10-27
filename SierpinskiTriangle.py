#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sun Apr 11 14:37:25 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.1 EJEMPLOS DE FRACTALES CLÁSICOS
        4.1.2 EL TRIÁNGULO DE SIERPINSKI
    
SierpinskiTriangle.py es un programa que sirve de apoyo a la sección 4.1.2 en la que se estudia
el triángulo de Sierpinski, considerado una versión bidimensional del conjunto de Cantor. Su finalidad es construir paso a paso el 
triángulo de Sierpinski. Al igual que con el resto de ejemplos, resulta interesante 
observar su propiedad de autosimilitud.
"""

import turtle

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


def DrawTriangle(a,b,c):
    """
    Dibuja un triángulo de vértices: a,b,c
    
    Parámetros
    ----------
    a: vértice del triángulo 
    b: vértice del triángulo
    c: vértice del triángulo
    """ 
    
    ax, ay = a
    bx, by = b 
    cx, cy = c
    
    #turtle.begin_fill() #Se utiliza para rellenar
    #turtle.color('black') #De color negro
           
    turtle.up()
    turtle.goto(ax,ay)
    turtle.down()
    turtle.goto(bx,by)
    turtle.goto(cx,cy)
    turtle.goto(ax,ay)
    turtle.up()
    
    #turtle.end_fill()
       
def SierpinskiTriangle(etapa,triangulo):
    """
    Representación del triángulo de Sierpinski
    
    Parámetros
    ----------
    etapa: nivel de profundidad, número de etapas
    triangulo: triángulo inicial    
    """ 
     
    #Pinto el triángulo inicial S_0
    a, b, c = triangulo
    DrawTriangle(a, b, c)
    
    #Si la etapa es la 0, ya hemos terminado 
    if etapa == 0:
        return
        
    #En caso contrario, ...         
    else:
        
        #Calculos los puntos medios de los tres lados del triángulo
        d = Midpoint(a, b)
        e = Midpoint(b, c)
        f = Midpoint(a, c)
        
        #Realizamos llamadas recursivas, teniendo en cuenta los nuevos vértices. 
        #Disminuimos en uno la etapa inicial. 
        
        turtle.begin_fill() #Se utiliza para rellenar
        turtle.color('black') #De color negro
        SierpinskiTriangle(etapa-1, [a,d,f]) #Llamada recursiva para generar el primer triángulo
        turtle.end_fill()
        
        turtle.begin_fill()
        turtle.color('black')
        SierpinskiTriangle(etapa-1, [d,b,e])#Llamada recursiva para generar el segundo triángulo
        turtle.end_fill()
        
        turtle.begin_fill()
        turtle.color('black')
        SierpinskiTriangle(etapa-1, [f,e,c])#Llamada recursiva para generar el tercer triángulo
        turtle.end_fill()    
    
#Eliminamos el cursor
turtle.ht()

#Velocidad 
turtle.speed(10)

triangulo=[[-200,-100],[0,300],[200,-100]]

for i in range (0,6):
    turtle.clear()
    turtle.title("Triángulo de Sierpinski en la iteración: " + str(i))
    SierpinskiTriangle(i, triangulo)
    if i==4:
        turtle.speed(0)
        
turtle.bye()
