#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:05:40 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.1 EJEMPLOS DE FRACTALES CLÁSICOS
        4.1.3 LA CURVA DE KOCH
    
KochCurve.py es un programa que sirve de apoyo a la sección 4.1.3 en la que se estudia
el fractal conocido como la curva de Koch. Su finalidad es construir paso a paso la curva de
Koch y su copo de nieve. Al igual que con el resto de ejemplos, resulta interesante 
observar su propiedad de autosimilitud.
"""

import turtle

def KochCurve(etapa,longitud):
    """
    Representación de la curva de Koch
    
    Parámetros
    ----------
    etapa: nivel de profundidad, número de etapas
    longitud: longitud de los segmentos    
    """ 

    #Si la etapa es 0
    if etapa == 0: 
        turtle.forward(longitud) #Segmento inicial k_0
        
    else:#En caso de no ser la etapa inicial, reemplazamos el tercio medio por 
         #dos segmentos formando un ángulo de 60º
         
        KochCurve(etapa-1, longitud/3)#LLamada recursiva para el primer segmento
        #Giro de 60º a la izquierda
        turtle.left(60)
        KochCurve(etapa-1, longitud/3)#LLamada recursiva para el segundo segmento
        #Giro de -120º a la izquierda 
        turtle.left(-120)
        KochCurve(etapa-1, longitud/3)#LLamada recursiva para el tercer segmento
        #Giro de 60º a la izquierda 
        turtle.left(60)
        KochCurve(etapa-1, longitud/3)#LLamada recursiva para el cuarto segmento


#Eliminamos el cursor
turtle.ht()

turtle.speed(10)

for i in range(0,6):
    
    turtle.clear()
    turtle.title("Curva de Koch en la iteración: " + str(i))
    
    turtle.up()
    turtle.goto(-300,0)
    turtle.down()
    
    KochCurve(i, (i+1)*100)
    
    if i==4:
        turtle.speed(0)

turtle.bye()    


turtle.speed(0)
turtle.clear()
turtle.up()
turtle.goto(-300,200)
turtle.down()

#Para generar el copo de nieve
for i in range (0,3):
    turtle.title("Copo de nieve de Koch ")
    KochCurve(4, 600)
    #Giro de 120 a la derecha 
    turtle.right(120)
 
turtle.bye()  

