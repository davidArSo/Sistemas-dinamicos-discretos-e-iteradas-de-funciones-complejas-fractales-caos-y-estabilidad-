#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sept 7 20:08:26 2021

@author: David Armenteros soto
"""

from color import *

class Light:
    """ Light representa la iluminación de la escena. Se trata de un punto de tres dimensiones con un cierto color """
    
    def __init__(self, position, color = WHITE):
        """ Constructor de la clase Light """
        
        self.position = position
        self.color=color
