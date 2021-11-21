#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sept 3 18:26:16 2021

@author: David Armenteros Soto 
"""

from color import *

class Image:
    """ Clase para crear y gestionar imágenes en formato PPM """
    
    def __init__(self, width, height):
        """ Constructor de la clase Image """
        
        self.width=width
        self.height=height
        #Inicializamos todos los píxeles de la imagen a blanco
        self.pixels= [ [ WHITE for i in range (width)]  for j in range (height)  ]
         
    def setPixel(self, row, col, color):
        """ Asigna un color a un pixel """
        
        self.pixels[col][row]=color
    
    @staticmethod
    def write_ppm_header(img_file, height=None, width=None ):
        """ Escribe unicamente la cabecera del fichero PPM.
            https://rosettacode.org/wiki/Bitmap/Write_a_PPM_file """
        
        img_file.write("P3 {} {}\n255\n".format(width, height))
    
    def write_ppm_pixels(self, img_file):
        """ Escribe el valor de los píxeles (color) en formato de archivo PPM.
            https://rosettacode.org/wiki/Bitmap/Write_a_PPM_file """
            
        #Convierte los colores al rango 0-255
        def to_Int255(c):
            return round(max(min(c,255), 0))
        
        for row in self.pixels:
            for color in row:
                #Escribimos los colores en formato (R, G, B)
                img_file.write("{} {} {} ".format(to_Int255(color.x),to_Int255(color.y), to_Int255(color.z)))
            img_file.write("\n")
            
    def write_ppm(self, img_file):
        """ Escribe el valor de los píxeles y la cabecera de un archivo PPM. """
        
        Image.write_ppm_header(img_file, self.height, self.width)
        self.write_ppm_pixels(img_file)
    
    