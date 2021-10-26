#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 4 20:47:33 2021

@author: David Armenteros Soto
"""
"""
3 SISTEMAS DINÁMICOS COMPLEJOS  
    3.3 APLICACIÓN DE LA TEORÍA DEL CONJUNTO DE JULIA AL MÉTODO DE NEWTON
    
ApplicationNewton-RapshonToJulia.py es un programa que  sirve de apoyo a la sección 3.3 en la que se aplicará la teoría
aprendida de los conjuntos de Julia al famoso método de Newton-Rapshon. Su finalidad es representar el fractal de Newton. 
Para ello se hará uso del método de Newton-Rapshon para la obtención de las raíces del polinomio cuadrático, cúbico, ... (en general de grado n). 
Posteriomente, se utilizarán técnicas similares a las ya mencionadas en teoría de conjuntos de Julia y Mandelbrot para su representación
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image, ImageDraw


def f_polynomial(z,n):
    """
    Definición de la función polinómica f(z)=z^n-1
    
    Parámetros
    ----------
    z: parámetro z de la función polinómica
    n: grado del polinonio 
    """ 
    return z**n-1

def GenerateNewtonFractal(n):
    """
    Generación del fractal de Newton
    
    Parámetros
    ----------
    n: grado del polinonio    
    """
    
    #Tamaño de la imagen (píxeles)
    x_pix=600
    y_pix=400
    
    #Valores máximo y mínimo de ambos ejes
    xmin, xmax= -2.5, 2.5
    ymin, ymax= -2.5, 2.5
    
    #Valores de largo y ancho de la imagen
    w = xmax - xmin
    h= ymax - ymin
    
    #Número de iteraciones máximas
    iter_max=100
    
    #Tamaño de la derivada
    h=1e-6
    
    #Error permitido
    error=1e-3
    
    #Creamos imágenes en el modo RGB (Red,Green,Blue) con tamaño el de los píxeles y color inicial (0,0,0) 
    im = Image.new('RGB', (x_pix, y_pix), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    #Recorremos los píxeles de la imagen
    for i in range (x_pix):
        for j in range (y_pix):
            #Posición del pixel en el plano complejo
            z=complex(i*w/(x_pix-1)+xmin,j*w/(y_pix-1)+ymin)
            
            #Aplicamos método de newton donde f(z)=z-p(z)/p'(z)
            for it in range(iter_max):
                #Calculamos el valor de la derivada
                dz=(f_polynomial(z+complex(h,h),n) - f_polynomial(z,n)   ) / complex(h,h)
                #Si el valor de la derivada es distinto de cero
                if dz != 0:
                    #Nuevo valor de f(z)
                    f_z=z-f_polynomial(z,n)/dz
                
                if abs(f_z-z) < error:
                    break
                z=f_z
             
            draw.point([i,j],(it % 4 * 64, it % 8 * 32, it % 16 * 16))
            
    #im.save('NewtonFractal.png', 'PNG')
    im.show()
                
            
for i in {2,3,4,5}:
    GenerateNewtonFractal(i)
