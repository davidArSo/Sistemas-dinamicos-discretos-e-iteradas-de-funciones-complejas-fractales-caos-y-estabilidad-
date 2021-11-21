#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sept 3 14:44:04 2021

@author: David Armenteros Soto
"""

from image import *
from rayTracer import RayTracer
from rayMarcher import RayMarcher
from light import Light
from composition import Composition
from point3D import Point3D
from vector3D import Vector3D
from scene import Scene
from sphere import Sphere
from mandelbulb import Mandelbulb
from juliabulb import JuliaBulb
from quaternion import Quaternion
from mandelbox import Mandelbox
from settings import *
from multiprocessing import *
import sys
import re 


def menu_ayuda():
     print (" ##################################### \n #  RENDERIZADOR DE FRACTALES EN 3D  # \n ##################################### \n")
     print (" David Armenteros Soto \n")
     print (" La siguiente aplicación es capaz de renderizar imágenes fractales mediante 'ray marching' con multiprocesamiento. Estos son los escenarios posibles: \n")
     print ("   - Esferas sobre un tablero de ajedrez \n")
     print ("   - Mandelbulb \n")
     print ("   - Cuaterniones de Julia (se disponen de 13 distintos, numerados del 1 al 13) \n")
     print ("   - Mandelbox \n")
     print (" ######################### \n # INSTRUCCIONES DE USO  # \n ######################### \n")
     print("\n")
     print(" ** Compile y ejecute con el siguiente comando: \n")
     print("    python main.py <Objeto3D> <Potencia> <Ruta de la imagen>.ppm -p <Número de procesos> \n")
     print("\n")
     print(" ** Los argumentos necesarios son: \n")
     print("    - <Objeto3D>: 'Sphere' - 'Mandelbulb' - 'Quaternionx' - 'Mandelbox' \n")
     print("    - <Potencia>: Potencia del Mandelbulb. El Mandelbulb clásico tiene potencia 8 (Añadir solo en el caso del Mandelbulb) \n")
     print("    - <Ruta de la imagen>.ppm: Imagen renderizada  \n")
     print("    - Opción -p <número de procesos>: Indica el número de procesos que intervienen en el renderizado. \n")
     print("                                      No es obligatorio, en caso de no añadirla el multiprocesamiento se hará con el número de CPUs del sistema \n")
     print("\n")
     print("** Ejemplos de Uso: \n")
     print("    python main.py Sphere Sphere.ppm -p 4 \n")
     print("    python main.py Mandelbulb 8 Mandelbulb.ppm \n")
     print("    python main.py Quaternion1 Quaternion1.ppm -p 6 \n")
     print("    python main.py Mandelbox Mandelbox.ppm \n")
     print("\n")
     print("** Aclaraciones: \n")
     print("    - Cada escena lleva asociada una resolución por defecto teniendo en cuenta la relación entre la calidad de la imagen y tiempo de renderizado  \n")
     print("\n")

def main():
    
    #Número de procesos por defecto, el número de cores del ordenador
    nprocs = cpu_count()
    
    if (len(sys.argv)==3 or len(sys.argv)==5)  and sys.argv[1] == 'Sphere' and re.match('.*.ppm$', sys.argv[2]) :
        
        #Si la longitud es 5, el número de procesos se nos da por parámetro
        if len(sys.argv)==5:
            if sys.argv[3] == '-p' and isinstance( int(sys.argv[4]), int):
                nprocs = int(sys.argv[4])
        
        #Escena del algoritmo
        scene= Scene(DEFAULT_CAMERA, CLASSIC_RAY_TRACING_OBJECTS, ILLUMINATION, HD_WIDTH, HD_HEIGHT, 1)
                
        #Renderizador
        engine= RayTracer()
        
        #Imagen renderizada
        print("Número de procesos: ", nprocs)
        print("Calidad de la imagen: HD ")
        print("Tiempo aproximado: 0-1 min  ")
        print("Renderizando ...")

        with open(sys.argv[2], "w") as img_file:
            engine.multiprocess_render(scene, nprocs, img_file)

        print("Completado con éxito")
                        
    elif (len(sys.argv)==4 or len(sys.argv)==6)  and sys.argv[1] == 'Mandelbulb' and isinstance( float(sys.argv[2]), float) and re.match('.*.ppm$', sys.argv[3]):
        
        #Si la longitud es 6, el número de procesos se nos dan por parámetro
        if len(sys.argv)==6:
            if sys.argv[4] == '-p' and isinstance( int(sys.argv[5]), int):
                nprocs = int(sys.argv[5])
        
        #Objeto que interviene en la escena del Mandelbulb
        MANDELBULB_OBJECTS=[Mandelbulb(float(sys.argv[2]),Composition(color=DARKGRAY, reflection=0.0))] 
        
        #Escena del algoritmo
        scene= Scene(MANDEL_CAMERA, MANDELBULB_OBJECTS, MANDEL_ILLUMINATION, HD_WIDTH, HD_HEIGHT, 3.5)
                
        #Renderizador
        engine= RayMarcher()
        
        #Imagen renderizada
        print("Número de procesos: ", nprocs)
        print("Calidad de la imagen: HD ")
        print("Tiempo aproximado: 2 min ")
        print("Renderizando ...")

        with open(sys.argv[3], "w") as img_file:
            engine.multiprocess_render(scene, nprocs, img_file)

        print("Completado con éxito")
            
    elif (len(sys.argv)==3 or len(sys.argv)==5) and re.match('^Quaternion([1-9]|1[0123])$', sys.argv[1]) and re.match('.*.ppm$', sys.argv[2]): 
        
        #Si la longitud es 5, el número de procesos se nos da por parámetro
        if len(sys.argv)==5:
            if sys.argv[3] == '-p' and isinstance( int(sys.argv[4]), int):
                nprocs = int(sys.argv[4])
                  
        """ Quaterniones entre los que poder elegir. Enlace para visualizar los cuaterniones:
            http://paulbourke.net/fractals/quatjulia/
        """
        
        Q1=Quaternion(-1,0.2,0,0)
        Q2=Quaternion(-0.291,-0.399,0.339,0.437)
        Q3=Quaternion(-0.2,0.4,-0.4,-0.4)
        Q4=Quaternion(-0.213,-0.0410,-0.563,-0.560)
        Q5=Quaternion(-0.2,0.6,0.2,0.2)
        Q6=Quaternion(-0.162,0.163,0.560,-0.599)
        Q7=Quaternion(-0.2,0.8,0,0)
        Q8=Quaternion(-0.445,0.339,-0.0889,-0.562)
        Q9=Quaternion(0.185,0.478,0.125,-0.392)
        Q10=Quaternion(-0.450,-0.447,0.181,0.306)
        Q11=Quaternion(-0.218,-0.113,-0.181,-0.496)
        Q12=Quaternion(-0.137,-0.630,-0.475,-0.046)
        Q13=Quaternion(-0.125,-0.256,0.847,0.0895)
        
        if sys.argv[1] == "Quaternion1":
            Q=Q1
        elif sys.argv[1] == "Quaternion2":
            Q=Q2
        elif sys.argv[1] == "Quaternion3":
            Q=Q3
        elif sys.argv[1] == "Quaternion4":
            Q=Q4
        elif sys.argv[1] == "Quaternion5":
            Q=Q5
        elif sys.argv[1] == "Quaternion6":
            Q=Q6
        elif sys.argv[1] == "Quaternion7":
            Q=Q7
        elif sys.argv[1] == "Quaternion8":
            Q=Q8
        elif sys.argv[1] == "Quaternion9":
            Q=Q9
        elif sys.argv[1] == "Quaternion10":
            Q=Q10
        elif sys.argv[1] == "Quaternion11":
            Q=Q11
        elif sys.argv[1] == "Quaternion12":
            Q=Q12
        elif sys.argv[1] == "Quaternion13":
            Q=Q13
             
        #Objetos que participan en la escena       
        JULIA_OBJECTS=[JuliaBulb(2,Q,Composition(GRAY,reflection=0.0))]  
                
        #Escena del algoritmo
        scene= Scene(JULIA_CAMERA, JULIA_OBJECTS, ILLUMINATION, SD_WIDTH, SD_HEIGHT, 2.5)
                
        #Renderizador
        engine= RayMarcher()
        
        #Imagen renderizada
        print("Número de procesos: ", nprocs)
        print("Calidad de la imagen: SD ")
        print("Tiempo aproximado: 2 min ")
        print("Renderizando ...")

        with open(sys.argv[2], "w") as img_file:
            engine.multiprocess_render(scene, nprocs, img_file)

        print("Completado con éxito")
        
    elif (len(sys.argv)==3 or len(sys.argv)==5)  and sys.argv[1] == 'Mandelbox' and re.match('.*.ppm$', sys.argv[2]): 
        
      #Si la longitud es 6, el número de procesos se nos dan por parámetro
        if len(sys.argv)==5:
            if sys.argv[3] == '-p' and isinstance( int(sys.argv[4]), int):
                nprocs = int(sys.argv[4])
                           
        #Escena del algoritmo
        scene= Scene(MANDELBOX_CAMERA, MANDELBOX_OBJECTS, ILLUMINATION, QVGA_WIDTH, QVGA_HEIGHT, 65.0)
                
        #Renderizador
        engine= RayMarcher()
        
        #Imagen renderizada
        print("Número de procesos: ", nprocs)
        print("Calidad de la imagen: QVGA ")
        print("Tiempo aproximado: 2-3 min ")
        print("Renderizando ...")

        with open(sys.argv[2], "w") as img_file:
            engine.multiprocess_render(scene, nprocs, img_file)

        print("Completado con éxito")
        
    else:
        print("\n Revise los argumentos, alguno es incorrecto \n")
        menu_ayuda()
        
    
        
if __name__ == '__main__':
    main()







