#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sept 3 14:37:17 2021

@author: David Armenteros Soto
"""

import math

class Vector3D:
    """ Clase para manipular vectores de tres dimensiones. Se utilizará para representar colores, puntos en 3D, ... """
        
    def __init__(self,x=0.0,y=0.0,z=0.0):
        """ Constructor de la clase Vector3D"""
        
        self.x=x
        self.y=y
        self.z=z
        
        
    """ Sobrecarga de operadores: """
    
    def __str__(self):
        """ Imprime por pantalla un Vector3D con formato (x,y,z)"""
        
        return "( {}, {}, {} )".format(self.x, self.y, self.z)
    
    def __add__(self,v):
        """ Suma de vectores"""
        
        return Vector3D(self.x + v.x , self.y + v.y, self.z + v.z )
    
    def __sub__(self,v):
        """ Resta de vectores """
        
        return Vector3D(self.x - v.x , self.y - v.y, self.z - v.z )
    
    def __mul__(self,n):
        """ Múltiplicación de un vector por un escalar """
        
        #Comprueba si 'n' es de tipo Vector3D
        assert not isinstance(n,Vector3D)
        return Vector3D(self.x * n, self.y * n, self.z *n)
    
    def __rmul__(self,n):
        """ Múltiplicación de un vector por un escalar """
        
        return self.__mul__(n)
    
    def __truediv__(self,n):
        """ División de un vector por un escalar """
        
        #Comprueba si 'n' es de tipo Vector3D
        assert not isinstance(n,Vector3D)
        return Vector3D(self.x/n, self.y/n, self.z/n)
           
    
    """ Operaciones con vectores: """
    
    def dot_product(self,v):
        """ Producto escalar """
        
        return self.x * v.x + self.y * v.y + self.z * v.z

    def magnitude(self):
        """ Norma del vector """
        
        #return math.sqrt(self.x**2+self.y**2+self.z**2)
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        """ Vector normalizado """
        
        m=self.magnitude()
        return self / m
    
    def cross_product(self,v):
        """ Producto vectorial """
        
        return Vector3D(self.y * v.z - self.z * v.y , self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x )
        