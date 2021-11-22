#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sept 7 14:17:44 2021

@author: David Armenteros Soto
"""

class Scene:
    """ Scene almacena información sobre los elementos que intervienen en el renderizado de imágenes mediante Ray tracing o Ray marching """
    
    def __init__(self, camera, objects, lights, width, height, zoom):
        """ Constructor de la clase Scene """
        
        self.camera=camera
        self.objects=objects
        self.lights=lights
        self.width=width
        self.height=height
        self.zoom=zoom
        