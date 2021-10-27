#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 8 21:09:58 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.1 EJEMPLOS DE FRACTALES CLÁSICOS 
        4.1.1 EL CONJUNTO DE CANTOR
    
CantorSet.py es un programa que sirve de apoyo a la sección 4.1.1 en la que se estudia
el primer fractal puro, conocido como el conjunto de Cantor.  Su finalidad es construir paso a paso este
fractal. Resulta interesante observar que puntos lo componen y verificar
la propiedad de autosimilitud. 
"""

import turtle

def cantorSet(izq,dercha,pos_inicial,distancia,iteraciones):
    """
    Representación del conjunto de Cantor
    
    Parámetros
    ----------
    izq: posición izquierda de inicio del segmento 
    dercha: posición derecha de inicio del segmento 
    pos_inicial: posición inicial
    distancia: distancia entre las líneas del conjunto de Cantor
    iteraciones: número de iteraciones a realizar
    
    Returns
    -------
    Para finalizar la recursividad
    
    """ 

    #Si el número de iteraciones es 0 dibujamos el segmento inicial
    if iteraciones == 0:
        turtle.up()
        turtle.goto(izq,(-pos_inicial+1)*distancia)
        turtle.down()
        turtle.goto(dercha,(-pos_inicial+1)*distancia)
        return
    
    #Si hay más de una iteración
    elif pos_inicial < iteraciones:
        
        #Dibujamos el segmento inicial
        turtle.up()
        turtle.goto(izq,(-pos_inicial+1)*distancia)
        turtle.down()
        turtle.goto(dercha,(-pos_inicial+1)*distancia)
        
        #Longitud del tercio del segmento 
        long=(dercha-izq)/3
        
        #Dibujamos el primer tercio 
        turtle.up()
        turtle.goto(izq,-pos_inicial*distancia)
        turtle.down()
        turtle.goto(izq+long,-pos_inicial*distancia)
        
        #Recursividad:
            #La posición derecha pasa a ser la izquierda más la longitud calculada
            #Aumentamos la posición inicial 
        cantorSet(izq,izq+long,pos_inicial+1,distancia,iteraciones)
        
        #Dibujamos el último tercio
        turtle.up()
        turtle.goto(izq+long*2,-pos_inicial*distancia)
        turtle.down()
        turtle.goto(dercha,-pos_inicial*distancia)
        
          #Recursividad:
            #La posición izquierda cambia y pasa a ser la izquierda más dos veces la longitud calculada
            #Aumentamos la posición inicial 
        cantorSet(izq+long*2,dercha,pos_inicial+1,distancia,iteraciones)
        
    else:
        #Acabamos la recursividad
        return


#Eliminamos el cursor
turtle.ht()

for i in range(0,8):
    turtle.clear()
    turtle.title("Conjunto de Cantor en la iteración: " + str(i))
    cantorSet(-250, 250, 0, 10, i)
    
turtle.bye()
