#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:25:14 2021

@author: David Armenteros Soto
"""
"""
3 SISTEMAS DINÁMICOS COMPLEJOS  
    3.1 EL CONJUNTO DE JULIA

JuliaSet.py es un programa que sirve de apoyo a la sección 3.1. Su finalidad es representar los conjuntos de 
Julia J_c a partir de distintos valores de c. En el siguiente código se encuenta una implementación
de los dos algoritmos mencionados en teoría:
    - Algoritmo para generar K_c en blanco y negro
    - Algoritmo de iteración inversa para generar K_c (cerco del conjunto de Julia)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image, ImageDraw

def GenerateJuliaSet(c,it_max, mode):
    """
    Representación del conjunto de Julia
    
    Parámetros
    ----------
    c: constante compleja c del mapa f_c(z)=z^2+c asociado al conjunto de Julia
    it_max: iteraciones máximas para su representación
    mode: algoritmo de representación. Puede ser 'BlackWhite' (blanco y negro) o BackwardIteration (cerco del conjunto de Julia)
    """ 
    
    #Número de píxeles de la imágen 
    x_pix=512
    y_pix=512
         
    #Valores máximo y mínimo de ambos ejes
    xmin, xmax= -1.5, 1.5
    ymin, ymax= -1.5, 1.5
    
    #Valores de largo y ancho de la imagen
    w = xmax - xmin
    h= ymax - ymin
    
    #Radio umbral 
    radio_umbral= max(2,abs(c))
    
    #Modos
    if(mode == 'BlackWhite'):
        #Creamos un array inicializado a cero, que contendrá los valores de los píxeles
        julia_p= np.zeros((x_pix, y_pix))
    elif (mode=='BackwardIteration'):
        #Creamos una imagen en modo RGB (Red,Green,Blue) con píxeles (x_pix,y_pix) y color inicial (0,0,0)
        im = Image.new('RGB', (x_pix, y_pix), (0, 0, 0))
        draw = ImageDraw.Draw(im)

    #Recorremos los píxeles de la imagen    
    for i in range (x_pix):
        for j in range (y_pix):
            #Posición del pixel en el plano complejo
            z=complex(i/x_pix*w+xmin,j/y_pix*h+ymin)
            #Iteramos el número complejo
            it=0
            #Criterio de escape
            while abs(z)<=radio_umbral and it<it_max:
                z=z**2+c
                it+=1
                
            if(mode=='BlackWhite'):
                #El valor del pixel será 0 o 255 (negro o blanco) dependiendo del valor absoluto del número complejo z
                if( abs(z)<=radio_umbral):
                    julia_p[i,j]=0

                else:
                    julia_p[i,j]=255
            elif(mode=='BackwardIteration'):
                #Dibujamos el punto. El color dependerá del número de iteraciones que se han necesitado para sobrepasar el radio umbral
                draw.point([i,j],(it % 4 * 64 , it %   8 * 32, it %   16 * 16))
     
    if(mode=='BlackWhite'):
        #Dibujamos el array con la herramienta matplotlib
        fig, ax = plt.subplots()
        ax.imshow(julia_p, interpolation='nearest', cmap=cm.gnuplot2)
        plt.axis('off')
        plt.show()
        #fig.savefig('juliaSet.png', dpi=500)
    elif(mode=='BackwardIteration'):
        imagen='JuliaSet_'+ str(c)+'.png'
        #im.save(imagen)
        im.show()


#Conjunto de Julia K_0
GenerateJuliaSet(complex(0,0),100,'BlackWhite')
GenerateJuliaSet(complex(0,0),1000,'BackwardIteration')


#Conjunto de Julia K_{-0.1+i*0.8}
GenerateJuliaSet(complex(-0.1,0.8),100,'BlackWhite')
GenerateJuliaSet(complex(-0.1,0.8),1000,'BackwardIteration')


#Conjunto de Julia K_{-0.39-i*0.58}
GenerateJuliaSet(complex(-0.39,-0.58),100,'BlackWhite')
GenerateJuliaSet(complex(-0.39,-0.58),1000,'BackwardIteration')   


#Conjunto de Julia K_{-0.5+i*0.5}
GenerateJuliaSet(complex(-0.5,0.5),100,'BlackWhite')
GenerateJuliaSet(complex(-0.5,0.5),1000,'BackwardIteration')   


#Conjunto de Julia K_{-1.1+i*0.1}
GenerateJuliaSet(complex(-1.1,0.1),100,'BlackWhite')
GenerateJuliaSet(complex(-1.1,0.1),1000,'BackwardIteration') 

#Conjunto de Julia K_{-0.2+i*0.75}
GenerateJuliaSet(complex(-0.2,0.75),100,'BlackWhite')
GenerateJuliaSet(complex(-0.2,0.75),1000,'BackwardIteration') 

#Propiedades topólogicas: 
    
#Conexo K_{0.377-i*0.248}
GenerateJuliaSet(complex(0.377,-0.248),100,'BlackWhite')
GenerateJuliaSet(complex(0.377,-0.248),1000,'BackwardIteration')

#Disconexo K_{-1.2*i}
GenerateJuliaSet(complex(0,-1.2),7,'BlackWhite')
GenerateJuliaSet(complex(0,-1.2),1000,'BackwardIteration')

