#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sept 24 20:40:01 2021

@author: David Armenteros Soto
"""

import math
from point3D import Point3D
from vector3D import Vector3D

MAX_ITERATIONS=15
INF=1e+30
DEPTH=2.0

class Mandelbulb:
    """ Mandelbulb es una versión 3D del conjunto de Mandelbrot en coordenadas esféricas """
    
    def __init__(self, power, composition):
        """ Constructor de la clase Mandelbulb"""
        
        self.power=power
        self.composition=composition
        
    def DistanceEstimator(self,point):
        """ Estima la distancia entre un punto y el Mandelbulb sin necesidad
            de calcular el punto de intersección entre un rayo y el fractal. Enlace útil:
            http://blog.hvidtfeldts.net/index.php/2011/09/distance-estimated-3d-fractals-v-the-mandelbulb-different-de-approximations/
        """
        
        #Punto de partida
        z=point
        #Derivada
        dr=1.0
        #Criterio de escape, norma del punto
        r=0.0
        #Para un determinado número máximo de iteraciones ... 
        for i in range (MAX_ITERATIONS):
            #Norma del punto 
            r=z.magnitude()
            #Algoritmo de escape 
            if r > DEPTH:
                break
            #Conversión a coordenadas polares
            #theta=math.atan2(math.sqrt(z.x**2+z.y**2), z.z)
            theta = math.acos(z.z / r)
            phi = math.atan2(z.y, z.x)
            dr=math.pow(r,self.power-1.0)*self.power*dr+1.0            
            #Rotación y escalado
            zr=math.pow(r,self.power)
            theta=theta*self.power
            phi=phi*self.power
            #Vuelta coordenadas cartesianas 
            z= Point3D(math.sin(theta)*math.cos(phi), math.sin(theta)*math.sin(phi), math.cos(theta))
            z = z * zr
            z = z + point
                        
        DE=0.5 * math.log(r) * r / dr
        
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
                     