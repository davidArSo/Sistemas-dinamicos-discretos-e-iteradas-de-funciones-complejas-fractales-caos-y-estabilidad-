#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 23:37:13 2021

@author: David Armenteros Soto
"""
import math
from point3D import Point3D
from vector3D import Vector3D

MAX_ITERATIONS=10
INF=1e+30

class Mandelbox:
    """ Mandelbox es un fractal en tres dimensiones introducido por Tom Lowe (2010)"""
    
    def __init__(self,composition):
        """ Constructor de la clase Mandelbox"""

        self.composition=composition
        
    def DistanceEstimator(self,point):
        """ Estima la distancia entre un punto y el Mandelbox sin necesidad
            de calcular el punto de intersección entre un rayo y el fractal. Enlace útil:
            http://blog.hvidtfeldts.net/index.php/2011/11/distance-estimated-3d-fractals-vi-the-mandelbox/
        """
        
        offset=point
        dr=1.0
        scale=2.0
        
        for n in range (MAX_ITERATIONS):
            point, dr= self.boxFold(point,dr)
            point,dr = self.sphereFold(point,dr)
            point = scale * point + offset
            dr = dr* abs(scale)+1.0

        r=point.magnitude()
        DE=r/abs(dr)
 		
        if DE == float('inf'):
            return INF
        
        return DE
              
    def boxFold(self,point,dr):
        px = max(min(point.x,1.0),-1.0) 
        py = max(min(point.y,1.0),-1.0) 
        pz = max(min(point.z,1.0),-1.0) 
        pxyz =Point3D(px,py,pz)
        
        p=pxyz*2.0-point
        
        return p,dr
    
    def sphereFold(self,point,dr):
        r2= point.magnitude()**2
        if r2 < 0.5:
            temp=2.0
            point*=temp
            dr*=temp
        elif r2 < 1.0:
            temp = 1.0 /r2
            point*=temp
            dr*=temp
    
        return point,dr
	

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

 