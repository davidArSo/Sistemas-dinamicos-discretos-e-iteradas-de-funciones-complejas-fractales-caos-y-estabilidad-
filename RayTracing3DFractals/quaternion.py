#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 2 13:38:42 2021

@author: David Armenteros Soto
"""

import math

class Quaternion:
    """ Clase para manipular vectores de cuatro dimensiones (cuaterniones) """
    
    def __init__(self,x=0.0,y=0.0,z=0.0, w=0.0):
        """ Constructor de la clase Quaternion """
        
        self.x=x
        self.y=y
        self.z=z
        self.w=w
        
        
    """ Sobrecarga de operadores: """
        
    def __str__(self):
        """ Imprime por pantalla un cuaternión con formato (x,y,z,w)"""
        
        return "( {}, {}, {}, {} )".format(self.x, self.y, self.z, self.w)
             
    def __add__(self,q):
        """ Suma de cuaterniones"""
        
        return Quaternion(self.x + q.x , self.y + q.y, self.z + q.z, self.w + q.w )
    
    def __sub__(self,q):
        """ Resta de cuaterniones"""
        
        return Quaternion(self.x - q.x , self.y - q.y, self.z - q.z, self.w - q.w )
    
    def __mul__(self,n):
        """ Múltiplicación de un cuaternión por un escalar """
        
        #Comprueba si 'n' es de tipo Quaternion
        assert not isinstance(n, Quaternion)
        return Quaternion(self.x * n, self.y * n, self.z *n, self.w*n)
        
    def __rmul__(self,n):
        """ Múltiplicación de un cuaternión por un escalar """
        
        return self.__mul__(n)
    
    def __truediv__(self,n):
        """ División de un cuaternión por un escalar """
        
        #Comprueba si 'n' es de tipo Quaternion
        assert not isinstance(n,Quaternion)
        return Quaternion(self.x/n, self.y/n, self.z/n, self.w/n)
    
    """ Operaciones con cuaterniones: """
    
    def dot_product(self,q):
        """ Producto escalar entre cuaterniones """
        
        return self.x * q.x + self.y * q.y + self.z * q.z + self.w *q.w
    
    def magnitude(self):
        """ Norma del cuaternión """
        
        #return math.sqrt(self.x**2+self.y**2+self.z**2+self.w**2)
        return math.sqrt(self.dot_product(self))
    
    def qmul(self, q):
        """ Multiplicación entre dos cuaterniones """
        
        return Quaternion (self.x * q.x - self.y * q.y - self.z * q.z - self.w * q.w
                           , self.y * q.x + self.x * q.y + self.z* q.w-self.w*q.z
                           , self.z * q.x + self.x * q.z + self.w * q.y - self.y * q.w
                           , self.w * q.x + self.x * q.w + self.y * q.z - self.z * q.y 
                           )
    def qsqr(self):
        """  Cuaternión al cuadrado """
        
        return self.qmul(self)
        
    def qconj(self):
        """ Cuaternión conjugado """
        
        return Quaternion(self.x, -self.y, -self.z, -self.w)
    
    