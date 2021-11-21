#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sept 7 14:22:14 2021

@author: David Armenteros Soto
"""

from image import *
from ray import Ray
from point3D import Point3D
from tqdm.auto import tqdm
#from alive_progress import alive_bar
import tempfile
from pathlib import Path
import shutil
from multiprocessing import *

class RayTracer:
    """ La clase rayTracer se encarga de dirigir el proceso de renderizado de objetos en 3D mediante 'Ray Tracing' """ 
    
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
                #Almacenamos los procesos
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
    
    def render (self, scene, hmin, hmax, part_file):
        """ Renderiza unas filas de píxeles a partir de un modelo 3D """
        
        w=scene.width
        h=scene.height
        
        """ Razón de aspecto de una imágen (aspect ratio), relación entre ancho y largo.
            https://medium.com/swlh/ray-tracing-from-scratch-in-python-41670e6a96f9
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
                im.setPixel(i,j-hmin,self.ray_tracing(ray,scene)) 

        with open(part_file, "w") as part_img_file:
            im.write_ppm_pixels(part_img_file)
    
    def ray_tracing(self, ray, scene, depth=0):
        """ Devuelve el color del objeto. Se tiene en cuenta el objeto y el punto de intersección con el rayo """
        
        #Color inicial
        color = BLACK
          
        #Objeto de intersección y distancia más cercana
        near_distance, IntersectionObject = self.nearIntersection(ray,scene)
           
        #Si no toca ningún objeto, devolvemos el color inicial
        if IntersectionObject is None:
            return color
               
        #Calculamos el punto de intersección. Un punto del rayo situado a una determinada distancia del origen
        IntersectionPoint = ray.RayPoint(near_distance)
        
        #Calculamos la normal al punto de intersección en la superficie
        IntersectionNormal=IntersectionObject.normalSurfaceAtPoint(IntersectionPoint)
        
        #Asociamos un color en función del objeto, el punto del rayo, la normal y la escena
        color += self.colorAtPoint(IntersectionObject , IntersectionPoint, IntersectionNormal, scene)
        
        #Reflejo de la luz 
        if depth < self.MAX_REFLECTION_DEPTH:
            ray_reflection_origin= IntersectionPoint + IntersectionNormal * self.DELTA
            ray_reflection_direction= ray.direction - 2* ray.direction.dot_product(IntersectionNormal)*IntersectionNormal
            ray_reflection= Ray(ray_reflection_origin, ray_reflection_direction)
            #Atenuamos el rayo de reflexión mediante el coeficiente de relfexión
            color += self.ray_tracing(ray_reflection, scene, depth + 1)*IntersectionObject.composition.reflection
        
        return color
                
    def nearIntersection( self, ray, scene):
         """ Calcula la distancia mínima entre el rayo y los objetos de la escena que lo intersecan """
        
         #Distancia y objeto inicial
         near_distance=None
         IntersectionObject=None
               
         #Recorremos los objetos de la escena
         for obj in scene.objects:
             #Por cada objeto de la escena, verificamos si el rayo interseca el objeto. En caso afirmativo, devolvemos la distancia con respecto al punto de intersección.
             distance = obj.intersectionWithRay(ray)
             #Si la distancia no es 'nula' (no es  None)
             if distance is not None:
                 #y el objeto es None o la distancia es menor que la distancía mínima
                 if IntersectionObject is None or distance < near_distance:
                     #Actualizamos la distancia más cercana y el objeto de intersección
                     near_distance=distance
                     IntersectionObject=obj
                     
         return near_distance, IntersectionObject
     
    def colorAtPoint(self, IntersectionObject, IntersectionPoint, IntersectionNormal, scene):
        """ Devuelve el color del punto de intersección teniendo en cuenta la normal en dicho punto """
        
        #Composición del objeto que interseca
        composition = IntersectionObject.composition
        #Color que forma parte de la composición del objeto que interseca
        objectColor=composition.colotAtPoint(IntersectionPoint)
        #Distancia a la cámara
        distanceCamToPoint = scene.camera - IntersectionPoint
        #Primero establecemos la luz ambiente
        color=composition.ambient_light * BLACK
        #Cálculos en función de las luces de la escena 
        for l in scene.lights:
            r = Ray (IntersectionPoint, l.position - IntersectionPoint)
            """ Sombras difusas mediante la ley del coseno de Lambert'. 
                https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-shading/diffuse-lambertian-shading
            """
            color += objectColor * composition.diffuse_light * max (IntersectionNormal.dot_product(r.direction),0) 
            """ Sombras  especulares mediante el modelo Blinn-Phong. 
                https://paroj.github.io/gltut/Illumination/Tut11%20BlinnPhong%20Model.html
                https://learnopengl.com/Advanced-Lighting/Advanced-Lighting
            """
            halfway_vector=(r.direction+distanceCamToPoint).normalize()
            specular_exponent=50
            color+=l.color*composition.specular_light*max (IntersectionNormal.dot_product(halfway_vector), 0)**specular_exponent
            
        return color
                   
                        