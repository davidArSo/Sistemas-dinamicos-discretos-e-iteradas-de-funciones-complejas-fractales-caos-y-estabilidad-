#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 2 18:43:46 2021

@author: David Armenteros Soto
"""

from vector3D import Vector3D
from quaternion import Quaternion
import math 

MAX_ITERATIONS=15
INF=1e+30
DEPTH=2.0

class JuliaBulb:
    """ Juliabulb es una versión 3D del conjunto de Julia cuadrático, es decir, asociado al mapa f(z)=z^2+c """
    
    def __init__(self, power, c, composition):
        """ Constructor de la clase Juliabulb"""
        
        self.power=power
        self.c=c
        self.composition=composition
                
    def DistanceEstimator(self,point):
        """ Estima la distancia entre un punto y el Juliabulb sin necesidad
            de calcular el punto de intersección entre un rayo y el fractal.
            https://iquilezles.org/www/articles/juliasets3d/juliasets3d.htm
        """
        
        #Punto de partida
        z = Quaternion (point.x, point.y, point.z, -0.1)
        #Derivada 
        dr=1.0
        #Criterio de escape
        r=z.magnitude()**2
        
        for i in range (MAX_ITERATIONS):
            dr *= 4.0*r
            z = z.qsqr() + self.c #z -> z^2 +c
            r = z.magnitude()**2
            
            if r >4.0:
                break
        
        DE=0.25*math.sqrt(r/dr)*math.log(r)
        
        if DE == float('inf'):
            return INF

        return DE
        
    def ValidDistanceEstimator(self, point):
        """ Distancia de estimación valida """
        
        DE= self.DistanceEstimator(point)
            
        if DE > 0:
            return DE
        else:
            return None
        
    def GradientNormal(self, EstimationSurfacePoint, ray):
        """Devuelve un vector normal a la superficie en un punto estimado. Enlace de interés:
            https://www.cs.drexel.edu/~david/Classes/Papers/rtqjs.pdf  
        """
        e = 2e-6
        
        Nx= self.DistanceEstimator(EstimationSurfacePoint + Vector3D(e,0,0))-self.DistanceEstimator(EstimationSurfacePoint - Vector3D(e,0,0)) 
        Ny= self.DistanceEstimator(EstimationSurfacePoint + Vector3D(0,e,0))-self.DistanceEstimator(EstimationSurfacePoint - Vector3D(0,e,0))
        Nz= self.DistanceEstimator(EstimationSurfacePoint + Vector3D(0,0,e))-self.DistanceEstimator(EstimationSurfacePoint - Vector3D(0,0,e))
           
        gradient = Vector3D (Nx, Ny, Nz)
        
        if gradient.magnitude() != 0:
            return gradient.normalize()
        else:
            return EstimationSurfacePoint.normalize()
    