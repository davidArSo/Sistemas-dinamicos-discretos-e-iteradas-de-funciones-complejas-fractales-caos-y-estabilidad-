#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sept 7 12:43:42 2021

@author: David Armenteros Soto
"""

import math

class Sphere:
    """ Sphere es un objeto en 3D. Se compone de radio, centro y composición """
    
    def __init__(self,center,radius, composition):
        """ Constructor de la clase Sphere """
        
        self.center=center
        self.radius=radius
        self.composition=composition
    
    def intersectionWithRay(self, ray):
        """ Comprueba si un rayo interseca a la esfera. En caso afirmativo, devuelve la distancia al punto de intersección. 
            https://medium.com/swlh/ray-tracing-from-scratch-in-python-41670e6a96f9 
        """
        
        #Distancia entre el origen del rayo y el centro de la esfera
        distanceSphereToRay=ray.origin-self.center
        #Cálculo del discriminante, para ver si el rayo interseca a la esfera
        a=1
        b=2*ray.direction.dot_product(distanceSphereToRay)
        c=distanceSphereToRay.dot_product(distanceSphereToRay) - self.radius**2
        discriminant=b**2-4*a*c
        
        #Si el discriminante es mayor o igual que 0, nos quedamos con la distancia más cercana a la cámara
        if discriminant >=0:
            distance=(-b-math.sqrt(discriminant))/2*a
            #Si la distancia es positiva, se devuelve
            if distance > 0:
                return distance
            
        return None
    
    def DistanceEstimator(self, point):
        """ Estima la distancia entre un punto y la esfera sin necesidad
            de calcular el punto de intersección (SDF para la esfera).
            http://jamie-wong.com/2016/07/15/ray-marching-signed-distance-functions/
        """
        
        distance = (point - self.center).magnitude() - self.radius
        
        if distance > 0:
            return distance
        else:
            return None
        
    def normalSurfaceAtPoint(self, surfacePoint):
        """Devuelve el vector normal a la superficie en un punto"""
        
        d=surfacePoint - self.center
        return d.normalize()
        