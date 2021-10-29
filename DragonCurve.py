#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:25:29 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.1 EJEMPLOS DE FRACTALES CLÁSICOS
        4.1.5 OTROS FRACTALES
            4.1.5.2 La curva del dragón
    
DragonCurve.py es un programa que sirve de apoyo a la sección 4.1.5.2 en la que se estudia
el fractal conocido como la curva del dragón. Su finalidad es construir paso a paso esta curva. 
Al igual que con el resto de ejemplos, resulta interesante observar su propiedad de autosimilitud.
"""

import turtle
import math
  
def DragonCurve(etapa,longitud, giro="derecha"):
    """
    Representa la curva del dragón 
    
    Parámetros
    ----------
    etapa: nivel de profundidad, número de etapas
    longitud: longitud de los segmentos  
    giro: giro de la tortuga 
    """  

    #Si la etapa es cero, solo dibujamos el segmento inicial
    if etapa==0:
       turtle.forward(longitud)
       return 
   
    #En caso de que la etapa no sea la cero...
    
    #Giro de 45 a izquierda o derecha 
    if giro == "derecha":
        turtle.right(45)
    else:
        turtle.left(45)
        
    #LLamada recursiva con giro a la derecha 
    DragonCurve(etapa-1, longitud/math.sqrt(2), giro="derecha")
    
    #Giro de 90 a izquierda o derecha
    if giro == "derecha":
        turtle.left(90)
    else:
        turtle.right(90)
        
    #Llamada recursiva con giro a la izquierda
    DragonCurve(etapa-1, longitud/math.sqrt(2), giro='izquierda')
    
    #Giro de 45 a derecha o izquierda
    if giro == "derecha":
        turtle.right(45)
    else:
        turtle.left(45)
        
#Eliminamos el cursor
turtle.ht()
turtle.speed('fastest')

for i in {0,1,2,6,9,12}:
    turtle.clear()
    turtle.title("Curva del dragón en la iteración: " + str(i))
        
    turtle.up()
    turtle.goto(0,100)
    turtle.down()
    
    DragonCurve(i, (i+1)*10)

turtle.bye()

   