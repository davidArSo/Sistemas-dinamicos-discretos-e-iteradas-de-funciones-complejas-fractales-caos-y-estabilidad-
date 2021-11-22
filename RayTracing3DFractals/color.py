#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sept 3 19:02:27 2021

@author: David Armenteros Soto
"""

from vector3D import Vector3D

class Color(Vector3D):
    """ Los colores se representan mediante tuplas de tres elementos (R,G,B). Hereda de la clase Vector3D """
    
    @classmethod
    def hex(cls,hexcolor="#000000"):
        """ Interpreta colores en hexadecimal. Se trata de un método de clase, ligado directamente a los atributos de la clase 
            que los contiene. Por convención se utiliza 'cls' en lugar 'self' """
        
        R= int (hexcolor[1:3],16)
        G= int (hexcolor[3:5],16)
        B= int (hexcolor[5:7],16)
        
        return cls (R,G,B)


""" Colores en hexadecimal: """

WHITE=Color.hex("#FFFFFF")
SOFTWHITE=Color.hex("#E6E6E6") 
BLACK=Color.hex("#000000")
RED=Color.hex("#FF0000")
GREEN=Color.hex("#00FF00")
LIGHTGREEN=Color.hex("#90EE90")
BLUE=Color.hex("#0000FF")
GRAY=Color.hex("#808080")
DARKGRAY=Color.hex("#606060")
TOMATO= Color.hex("#FF6347")
SKYBLUE= Color.hex("#87CEEB")
STEELBLUE=Color.hex("#4682B4")
BROWN=Color.hex("#A52A2A")
DARKBROWN=Color.hex("#654321") 
LIGHTBROWN= Color.hex("#C4A484")
INDIGO= Color.hex("#4B0082")
FIREBRICK= Color.hex("#B22222") 
YELLOW= Color.hex("#BF5C33B") 
GOLD=Color.hex("#FFD700") 
COBRE=Color.hex("#B87333") 

"""
Colores en formato (R, G, B):

WHITE= Color (255, 255, 255)
BLACK= Color (0, 0, 0)
RED= Color (255, 0, 0)
GREEN= Color (0, 255, 0)
BLUE= Color (0, 0, 255)
"""