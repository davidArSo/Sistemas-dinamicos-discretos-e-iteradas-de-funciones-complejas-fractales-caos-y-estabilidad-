#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:13:30 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.1 EJEMPLOS DE FRACTALES CLÁSICOS
        4.1.4 El CUADRADO DE KOCH
    
KochSquare.py es un programa que sirve de apoyo a la sección 4.1.4 en la que se estudia
el fractal conocido como el cuadrado de Koch, una variación de la ya conocida
curva de Koch. Su finalidad es construir paso a paso este fractal. Al igual que con el resto de ejemplos, 
resulta interesante observar su propiedad de autosimilitud.
"""

import turtle

def KochSquare(etapa,longitud):
    """
    Representación del cuadrado de Koch
    
    Parámetros
    ----------
    etapa: nivel de profundidad, número de etapas
    longitud: longitud de los segmentos    
    """ 
    
    #Si la etapa es 0
    if etapa == 0:
        turtle.forward(longitud)#Segmento inicial
    else:
        KochSquare(etapa-1, longitud/3)#LLamada recursiva para el primer segmento
        #Giro de 90º a la izquierda
        turtle.left(90)
        KochSquare(etapa-1, longitud/3)#LLamada recursiva para el segundo segmento
        #Giro de 270º a la izquierda
        turtle.left(270)
        KochSquare(etapa-1, longitud/3)#LLamada recursiva para el tercer segmento
        #Giro de 270º a la izquierda
        turtle.left(270)
        KochSquare(etapa-1, longitud/3)#LLamada recursiva para el cuarto segmento
        #Giro de 90º a la izquierda
        turtle.left(90)
        KochSquare(etapa-1, longitud/3)#LLamada recursiva para el quinto segmento

        
#Eliminamos el cursor
turtle.ht()

turtle.speed(8)

for i in range(0,6):
    turtle.clear()
    turtle.title("Cuadrado de Koch en la iteración: " + str(i))
    
    turtle.up()
    turtle.goto(-200,200)
    turtle.down()
    for j in range (0,4):
        KochSquare(i, 400)
        turtle.right(90)
        
    if i==2:
        turtle.speed(0)

turtle.bye()