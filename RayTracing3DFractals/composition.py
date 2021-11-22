#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sept 7 20:19:31 2021

@author: David Armenteros Soto
"""

from color import *

class Composition:
    """ Composition almacena información relativa al objeto a renderizar sobre el color, luz ambiental, iluminación difusa, iluminación especular y reflejos """
         
    def __init__(self, color= WHITE, ambient_light= 0.05, diffuse_light=1.0, specular_light=1.0, reflection=0.5):
        """ Constructor de la clase Composition """
        
        self.color = color
        self.ambient_light=ambient_light
        self.diffuse_light=diffuse_light
        self.specular_light=specular_light
        self.reflection=reflection

    def colotAtPoint(self, point):
        """ Devuelve el color del objeto """
        
        return self.color
    
class ChessBoardComposition:
    """ ChessBoardComposition almacena información sobre la composición del 'plano' de la escena. Contiene patrones de un tablero de ajedrez """
         
    def __init__(self, color1= WHITE, color2= BLACK, ambient_light= 0.05, diffuse_light=1.0, specular_light=1.0, reflection=0.5):
        """ Constructor de la clase ChessBoardComposition """
        
        self.color1 = color1
        self.color2=color2
        self.ambient_light=ambient_light
        self.diffuse_light=diffuse_light
        self.specular_light=specular_light
        self.reflection=reflection

    def colotAtPoint(self, point):
        """ Devuelve el color del objeto dada una posición. """
        """
        Para generar un tablero de ajedrez en el plano y=0, hay que tener en cuenta lo siguiente:
        Dado un punto (x,0,z), si el resto de dividir la coordenada x y z entre 2 es el mismo entonces se le asignará un color. 
        En caso de que no coincidan se le asignará otro. Si nos fijamos en un tablero de ajedrez de 8x8, las casillas A1, C1, B2 tienen
        el mismo color y las casillas A2, A4, B1 tienen otro.
        """
            
        if int((point.x+0.5) *3.0 ) % 2 == int((point.z) *3.0 ) % 2:
            return self.color1
        else:
            return self.color2

