#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sept 24 23:01:27 2021

@author: David Armenteros Soto
"""

from image import *
from ray import Ray
from point3D import Point3D
from tqdm.auto import tqdm
#from alive_progress import alive_bar
import math
import tempfile
from pathlib import Path
import shutil
from multiprocessing import *

MAX_MARCHES=150
EPSILON=0.01

class RayMarcher:
    """ La clase RayMarcher se encarga de dirigir el proceso de renderizado de objetos en 3D mediante 'Ray Marching' a imágenes en 2D """ 
    
    MAX_REFLECTION_DEPTH=5
    DELTA=0.0001
    
    def multiprocess_render (self, scene, nprocs, img_file):
        """ Renderiza un objeto 3D mediante multiprocesamiento """
        
        def split(rows, nprocs):
            """ Divide filas de píxeles entre el número de procesos de manera igualitaria 
                https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
            """
            
            div, rest= divmod(rows,nprocs)
            return [(i * div + min(i,rest), (i+1)*div + min(i+1,rest)) for i in range (nprocs) ]
            
        #Dimensiones de la imagen
        w = scene.width
        h = scene.height
        #Repartimos la altura de la imagen (filas de píxeles) entre los procesos 
        ranges = split(h,nprocs)
        #Creamos un directorio temporal para almacenar las distintas partes de la imagen
        tmp_dir=Path(tempfile.mkdtemp())
        #Nombres de los ficheros temporales
        tmp_file= "part_{}.temp"
        #Array para almacenar los distintos procesos 
        procs=[]
        
        try:
            for hmin,hmax in ranges:
                #PATH del fichero temporal
                part_file = tmp_dir / tmp_file.format(hmin)
                #Almacenmos los procesos
                procs.append(Process(target=self.render, args=(scene,hmin,hmax,part_file)))
            
            #Comenzamos todos los procesos
            for p in procs:
                p.start()
            #Esperamos a que todos terminen
            #with alive_bar (len(procs)) as bar:
            for p in procs:
                p.join()
                #bar()
                    
            #Juntamos todas las imágenes temporales en una 
            Image.write_ppm_header(img_file, h, w)
            for hmin, hmax in ranges:
                part_file = tmp_dir / tmp_file.format(hmin)
                img_file.write(open (part_file, "r").read())
            
        finally:
            #Para finalizar, eliminamos el directorio temportal
            shutil.rmtree(tmp_dir)
    
    def render (self,scene, hmin, hmax, part_file):
        "Renderiza un objeto 3D mediante 'Ray marching' "
        
        w=scene.width
        h=scene.height
        
        """ Razón de aspecto de una imágen (aspect ratio), relación entre ancho y largo. Enlaces de interés:
            https://medium.com/swlh/ray-tracing-from-scratch-in-python-41670e6a96f9
            https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-generating-camera-rays/generating-camera-rays
        """
        aspect_ratio= float(w)/h
        
        xmin=-scene.zoom
        xmax=scene.zoom
        ymin=-scene.zoom/ aspect_ratio
        ymax=scene.zoom/aspect_ratio
    
        cam=scene.camera
        im=Image(w,hmax-hmin)
        
        #Lanzamos distintos rayos a la parte de la escena designada, recorremos esos píxeles y asociamos colores
        for j in tqdm(range (hmin,hmax)):
            y_pixel= ymin + j * (ymax - ymin)/(h-1)
            for i in range (w):
                x_pixel = xmin + i* (xmax-xmin)/(w-1)
                ray= Ray (cam, Point3D(x_pixel,y_pixel) - cam)
                im.setPixel(i,j-hmin,self.ray_marching(ray,scene)) 

        with open(part_file, "w") as part_img_file:
            im.write_ppm_pixels(part_img_file)
            
            
    def ray_marching(self,ray,scene,depth=0):
        """ Devuelve el color del objeto, según una estimación de la distancia """
        
        #Color inicial
        color = BLACK
        
        #Estimación de la distancia
        EstimationDistance, EstimationObject = self.nearEstimationDistance(ray,scene)
        
        #Si no aproxima  ningún objeto, devolvemos el color inicial
        if EstimationObject is None :
            return color
        
        #Calculamos el punto del rayo situado a la distancia de estimación calculada
        EstimationPoint = ray.RayPoint(EstimationDistance)
        
        #Calculamos la normal al punto de estimación en la superficie
        EstimationNormal=EstimationObject.GradientNormal(EstimationPoint,ray)
        
        #Asociamos un color en función del punto estimado.
        color += self.colorAtPoint(EstimationObject , EstimationPoint, EstimationNormal, scene)
        
        """ Reflejo de la luz. Enlaces de interés:
            https://raytracing.github.io/books/RayTracingInOneWeekend.html#metal/modelinglightscatterandreflectance
        """
        if EstimationObject.composition.reflection != 0:
            if depth < self.MAX_REFLECTION_DEPTH:
                ray_reflection_origin= EstimationPoint + EstimationNormal * self.DELTA
                ray_reflection_direction= ray.direction - 2* ray.direction.dot_product(EstimationNormal)*EstimationNormal
                ray_reflection= Ray(ray_reflection_origin, ray_reflection_direction)
                #Atenuamos el rayo de reflexión mediante el coeficiente de relfexión
                color += self.ray_marching(ray_reflection, scene, depth + 1)*EstimationObject.composition.reflection
        
        return color
    
    def nearEstimationDistance( self, ray, scene):
         """ Calcula la distancia mínima de estimación """
        
         #Distancia y objeto inicial
         near_EstimationDistance=None
         EstimationObject=None
         
         #Recorremos los objetos de la escena 
         for obj in scene.objects:
             #Distancia total
             total_distance=0.0
             #Calculamos la distancia de estimación con el rayo en un número de pasos de 'Ray marching' (marchas)
             for i in range(MAX_MARCHES):
                distance_estimation = obj.ValidDistanceEstimator(ray.RayPoint(total_distance))
                if distance_estimation is None:
                    total_distance=None
                    near_EstimationDistance=None
                    EstimationObject=None
                    break
                
                total_distance+=distance_estimation
                #y el objeto es None o la distancia de estimación es menor que la distancía mínima
                if  distance_estimation < EPSILON:
                    break
                
             if total_distance is not None:
                 if EstimationObject is None or total_distance < near_EstimationDistance:
                     near_EstimationDistance=total_distance
                     EstimationObject=obj
                 
         return near_EstimationDistance, EstimationObject
     
    def colorAtPoint(self, EstimationObject, EstimationPoint, EstimationNormal, scene):
        """ Devuelve el color en el punto """
        
        #Composición del objeto a estimar
        composition = EstimationObject.composition
        
        #Color que forma parte de la composición del objeto a estimar
        objectColor=composition.colotAtPoint(EstimationPoint)
        
        #Distancia a la cámara
        distanceCamToPoint = scene.camera - EstimationPoint
        
        #Primero establecemos la luz ambiente
        color=composition.ambient_light * BLACK
        
        #Cálculos de la luz. Por cada luz de la escena ...
        for l in scene.lights:
            r = Ray (EstimationPoint, l.position - EstimationPoint)
            """ Sombras difusas mediante la ley del coseno de Lambert'. Enlace de interés:
                https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-shading/diffuse-lambertian-shading
            """
            color += objectColor * composition.diffuse_light * max (EstimationNormal.dot_product(r.direction),0) 
            """ Sombras  especulares mediante el modelo Blinn-Phong. Enlaces de interés:
                https://paroj.github.io/gltut/Illumination/Tut11%20BlinnPhong%20Model.html
                https://learnopengl.com/Advanced-Lighting/Advanced-Lighting
            """
            halfway_vector=(r.direction+distanceCamToPoint).normalize()
            specular_exponent=50
            color+=l.color*composition.specular_light*max (EstimationNormal.dot_product(halfway_vector), 0)**specular_exponent

        return color
        

