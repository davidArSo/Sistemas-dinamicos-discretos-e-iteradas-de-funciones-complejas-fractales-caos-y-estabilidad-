#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:36:50 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.1 EJEMPLOS DE FRACTALES CLÁSICOS 
        4.1.5 OTROS FRACTALES
            4.1.5.1 La curva de Lévy

LevyCurve.py es un programa que sirve de apoyo a la sección 4.1.5.1 en la que se estudia
el fractal conocido como la curva de Lévy. Su finalidad es construir paso a paso esta curva. Al igual que 
con el resto de ejemplos, resulta interesante observar su propiedad de autosimilitud.
"""

import turtle
import math

def LevyCurve(etapa,longitud):
    """
    Representa la curva de Lévy
    
    Parámetros
    ----------
    etapa: nivel de profundidad, número de etapas
    longitud: longitud de los segmentos    
    """  
    
    #Si la etapa es 0
    if etapa == 0:
        turtle.forward(longitud)#Segmento inicial
    else:
        #Giro de 45 a la izquierda
        turtle.left(45)
        LevyCurve(etapa-1,longitud/math.sqrt(2))#Primera recursión
        #Giro de 90 a la derecha
        turtle.right(90)
        LevyCurve(etapa-1,longitud/math.sqrt(2))#Segunda Recursión
        #Giro de 45 a la izquierda
        turtle.left(45)
             
#Eliminamos el cursor
turtle.ht()

for i in {0,1,2,4,6,9}:
    turtle.clear()
    turtle.title("Conjunto de Lévy en la iteración: " + str(i))
    
    turtle.up()
    turtle.goto(-200,0)
    turtle.down()
    
    if(i<=4):
        l=100
    else:
        turtle.speed(0)
        l=200
    
    LevyCurve(i, l)

turtle.bye()
