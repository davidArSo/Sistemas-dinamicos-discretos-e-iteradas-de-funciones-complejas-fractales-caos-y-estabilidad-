#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:58:32 2021

@author: David Armenteros Soto
"""

from image import *
from light import Light
from composition import Composition, ChessBoardComposition
from point3D import Point3D
from vector3D import Vector3D
from scene import Scene
from sphere import Sphere
from mandelbox import Mandelbox

#########################
### AJUSTES DE INICIO ###
#########################


##########                
# IMAGEN #
##########
#Resoluciones:

#Resolución QVGA    
QVGA_WIDTH=320
QVGA_HEIGHT=240

#Resolución SD
SD_WIDTH=640
SD_HEIGHT=480
    
#Resolcuión qHD
qHD_WIDTH=960
qHD_HEIGHT=540

#Resolución HD
HD_WIDTH=1280
HD_HEIGHT=720
    
###########                
# CÁMARAS #
###########
#Posición por defecto de la cámara (escena de las esferas)
DEFAULT_CAMERA= Vector3D(0,0,-2)
#Posición de la cámara para el Mandelbulb visto desde arriba
MANDEL_CAMERA=Vector3D(0,0,-2.5)
#Posición de la cámara para el Mandelbulb visto desde un lateral
MANDEL_CAMERA=Vector3D(0,3,-3.5)
#Posición de la cámara para los distintos cuaterniones de Julia
JULIA_CAMERA= Vector3D(0,-1,-3)
#Posición de la cámara para el Mandelbox
MANDELBOX_CAMERA= Vector3D(0,0,-7)

###############               
# ILUMINACIÓN #
###############
#Iluminación de la escenas
ILLUMINATION=[Light(Point3D(1.5,-0.5,-10.0), WHITE), Light(Point3D(-0.5,-10.5,0.0), SOFTWHITE)]
MANDEL_ILLUMINATION=[Light(Point3D(1.5,-0.5,-10.0), WHITE)]


###########               
# OBJETOS #
###########
#Objetos que intervienen en el Ray tracing clásico
CLASSIC_RAY_TRACING_OBJECTS=[
    #Plano con tablero de ajedrez
    Sphere(Point3D(0,1e+5+0.5,1),1e+5, ChessBoardComposition(color1=BLACK, color2=WHITE, ambient_light=0.2, reflection=0.2 )),
    #Bola azul
    Sphere(Point3D(0.5,-0.1,1.25),0.6,Composition(BLUE)),
    #Bola color indigo
    Sphere(Point3D(-0.75,-0.1,2.5),0.6,Composition(INDIGO)),
    #Bola roja
    Sphere(Point3D(-1.65,0,2.0),0.4,Composition(RED)),
    #Bola verde
    Sphere(Point3D(-1.25,0,0.25),0.3,Composition(GREEN)),
    #Bola amarillenta
    Sphere(Point3D(1.5,0,2.25),0.5,Composition(YELLOW)),
    ]

#Objeto que interviene en la escena del Mandelbulb
MANDELBOX_OBJECTS=[Mandelbox(Composition(color=COBRE, reflection=0.0))] 



