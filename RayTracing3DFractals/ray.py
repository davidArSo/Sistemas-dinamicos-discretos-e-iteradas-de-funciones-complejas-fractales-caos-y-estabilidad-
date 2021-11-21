#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sept 7 13:05:26 2021

@author: David Armenteros soto
"""
 
class Ray:
    """ Un rayo es una recta con un punto de origen y una dirección normalizada """
    
    def __init__(self, origin, direction):
        """ Constructor de la clase Ray """
        
        self.origin=origin
        self.direction=direction.normalize()
        
    def RayPoint(self, distance):
        """ Devuelve un punto del rayo situado a una distancia del origen """
        
        return self.origin + self.direction * distance
    
