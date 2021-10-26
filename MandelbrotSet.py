#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:56:27 2021

@author: David Armenteros Soto
"""
"""
3 SISTEMAS DINÁMICOS COMPLEJOS  
    3.2 EL CONJUNTO DE MANDELBROT
    
MandelbrotSet.py es un programa que sirve de apoyo a la sección 3.2. Su finalidad es representar 
el conjunto de Mandelbrot. Se puede apreciar como M es conexo y como es un subconjunto del disco de radio 2, así como los distintos bulbos que 
se forman, ... El conjunto de Mandelbrot sirve de introducción al mundo de los fractales, siendo
un claro ejemplo de ello. 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image, ImageDraw
import math

#1. Pasamos por argumento un número fijo de iteraciones máximas
def GenerateMandelbrotSet(it_max,mode):
    """
    Representación del conjunto de Mandelbrot
    
    Parámetros
    ----------
    it_max: iteraciones máximas para su representación
    mode: algoritmo de representación. Puede ser 'BlackWhite' (blanco y negro) o 'color' 
    
    """ 
    
    #Tamaño de la imagen (píxeles)
    x_pix=512
    y_pix=512
    
    if(mode=="BlackWhite"):
        #2. Tomamos un subconjunto que contenga al disco cerrado de radio 2
        xmin, xmax= -2, 1
        ymin, ymax= -2, 1
    elif (mode=="Color"):
        #2. Tomamos un subconjunto que contenga al disco cerrado de radio 2
        xmin, xmax= -2, 1
        ymin, ymax= -2, 1.5
        
    #Valores de largo y ancho de la imagen
    w = xmax - xmin
    h= ymax - ymin
    
    if(mode == "BlackWhite"):
       #Creamos un array inicializado a cero, que contendrá los valores de los píxeles
        mandelbrot_p= np.zeros((x_pix, y_pix))
    elif (mode == "Color"):
        #Creamos una imagen en el modo RGB (Red,Green,Blue) con tamaño el de los píxeles y color inicial (0,0,0) 
        im = Image.new('RGB', (x_pix, y_pix), (0, 0, 0))
        draw = ImageDraw.Draw(im)
    
    #Recorremos los píxeles de la imagen
    for i in range (x_pix):
        for j in range (y_pix):
            if (mode == "BlackWhite"):
                #Posición del pixel en el plano complejo
                c=complex(j/y_pix*h+ymin,i/x_pix*w+xmin)
            elif (mode == "Color"):
                c=complex(i/x_pix*w+xmin,j/y_pix*h+ymin)
            
            #3. Función de mandelbrot: dado un z=(0,0) inicial, iteramos el valor de c obteniendo así c,c^2, c+c^2, ... 
            z=complex(0,0)
            it=0
            while abs(z)<=2 and it<it_max:
                 z=z**2+c
                 it=it+1
            if (mode == "BlackWhite"):
                #4. Si alguna iteración sale del disco, dejamos de iterar y pintamos el punto de blanco, en otro caso, lo pintamos de negro.
                if(abs(z)<=2):
                   mandelbrot_p[i,j]=0 
                else:
                   mandelbrot_p[i,j]=255
            elif (mode == "Color"):
                #4. El color del punto dependerá del número de iteraciones
                draw.point([i,j],(it % 4 * 64  , it % 8 * 32  , it % 16 * 16))
            
    if (mode == "BlackWhite"):      
        #Dibujamos el array con la herramienta matplotlib
        fig, ax = plt.subplots()
        ax.imshow(mandelbrot_p, interpolation='nearest', cmap=cm.gnuplot2)
        plt.axis('off')
        plt.show()
        #fig.savefig('MandelbrotSetBlackWhite.png', dpi=500)
    elif (mode == "Color"):
        #im.save('MandelbrotSetColor.png', 'PNG')
        im.show()
  
        
GenerateMandelbrotSet(1000,'BlackWhite')
GenerateMandelbrotSet(1000,'Color')
