#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 3 18:02:21 2021
@author: David Armenteros Soto 
"""
"""
5 Dimensión fractal
    5.1 Dimensión box counting
        
El presente programa sirve de apoyo la sección 5.1. El objetivo del programa es 
calcular la dimensión box counting de forma computacional. Este programa se pondrá
a prueba con diferentes fractales donde los resultados prácticos se asemejan a los teóricos (dimensión
de Hausdorff). Es normal que no proporcionen los resultados exactos  porque a la hora de aplicar
el algoritmo tomamos un objeto fractal en una iteración concreta. Lo ideal sería considerar una etapa 
lo más próxima al infinito, sin embargo, se necesitaría mucho tiempo para ello.
"""

import numpy as np 
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

"""
En primer lugar, es necesario convertir la imagen fractal en modo RGB a una en
escala de grises. Posteriormente,  convertimos esta última imagen en un array binario, donde 
0 representa negro y 1 representa blanco. Esto es imprescindible para distinguir 
la frontera del objeto y poder contar las cajas que cubren el mismo.
"""

def RGB_To_BinaryGray(rgb):
    """
    Convierte una imagen en modo RGB a binaria

    Parámetros
    ----------
    rgb: imagen en modo RGB
        
    Returns
    -------
    imagen en binario
    """ 
    
    #Separamos los canales RGB y convertimos la imagen a escala de grises:
    #https://www.kite.com/python/answers/how-to-convert-an-image-from-rgb-to-grayscale-in-python
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gris = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    #Transformamos la imagen en un array binario con un cierto valor umbral. 
    #Gracias al valor umbral, convertimos los valores de los píxeles en binarios. De tal forma que, si el valor del píxel es menor 
    #que el umbral entonces se convertirá en 0 (negro), en el caso contrario será 1 (blanco)
    #https://datacarpentry.org/image-processing/07-thresholding/
    
    umbral=0.7
    binario = (gris < umbral)

    return binario

"""
A continuación, nos disponemos a contar el número de cajas que cubren el fractal. Tenemos una imagen binaria 'img' 
con valores de pixeles: 0 o 1. Se caclula la suma de todos los pixeles por cada bloque 'dim_caja x dim_caja' 
y contamos cuantos bloques tienen una suma entre 0 (todos los píxeles de este bloque son negros) y dim_caja*dim_caja(todos los píxeles de este bloque son blancos).
Si el bloque cumple esta condición entonces cubre pixeles blancos y negros, en otras palabras, cubre
la frontera del objeto.
"""

def conteo_cajas(img, dim_caja):
    """
    Cuenta el número de cajas que cubren un fractal

    Parámetros
    ----------
    img: imagen fractal
    dim_caja: dimensión de la caja
        
    Returns
    -------
    Número de cajas que cubren el fractal
    """ 
    
    #Dada una matríz de píxeles de tamaño img.shape[0] x img.shape[1], calcumos la suma por bloques de dim_caja x dim_caja 
    #Ejercicio 65 de : https://pythonworld.ru/numpy/100-exercises.html
    img_reducida = np.add.reduceat(np.add.reduceat(img, np.arange(0, img.shape[0], dim_caja), axis=0),np.arange(0, img.shape[1], dim_caja), axis=1)

    num_cajas=0
    for i in range (img_reducida.shape[0]):
        for j in range (img_reducida.shape[1]):
            if img_reducida[i][j] >0 and img_reducida[i][j] < dim_caja*dim_caja:
                num_cajas+=1
        
    return num_cajas
    

def BoxCountingDimension(img):
    """
    Algoritmo Box counting.
    
    Parámetros
    ----------
    img: imagen fractal
        
    Returns
    -------
    Dimensión fractal resultante 
    """ 
    
    #Tomamos la dimensión más pequeña entre largo y ancho 
    dim_min = min(img.shape)
    #Tomamos la mayor potencia de 2 menor o igual que la dimensión mínima
    n = 2**np.floor(np.log(dim_min)/np.log(2))
    #Sacamos el exponente
    n = int(np.log(n)/np.log(2))
    #Construimos las dimensiones de las cajas que irán de 2**n a 2**1
    dimensiones = 2**np.arange(n,1,-1)
    #Array donde almacenaremos el número de cajas 
    cajas = []
    
    #Aplicamos el conteo de cajas a cada una de las dimensiones 
    for dimension in dimensiones:
        num_cajas=conteo_cajas(img, dimension)
        cajas.append(num_cajas)
        print("Si la dimensión de la caja es de ", dimension, " píxeles, el número de cajas es ", num_cajas )
     
    #Representamos el número de cajas en relación a su dimensión
    plt.plot(dimensiones, cajas, '^',marker="o" )
    plt.xlabel("Dimensión de la caja: $2^n$ n=1, 2, 3, ...")
    plt.ylabel("Número de Cajas $N_n(A)$")
    plt.show()

    #Aplicación de la función logarítmica dela gráfica anterior 
    plt.plot(-np.log(dimensiones), np.log(cajas),'^', marker="o", color="orange",label=" Puntos obtenidos al aplicar logaritmos")
    #Ajuste polinomial de grado 1 a las funciones logarítmicas 
    coeficientes = np.polyfit(-np.log(dimensiones), np.log(cajas), 1)
    plt.plot(-np.log(dimensiones), [coeficientes[0]*i+coeficientes[1] for i in -np.log(dimensiones) ], color="black", label="Ajuste polinomial de mínimos cuadrados")
    plt.xlabel("- ln($2^n$) n=1, 2, 3, ... ")
    plt.ylabel("ln($N_n(A)$)")
    plt.legend(loc='best')
    plt.show()
    #print("La recta de mejor ajuste de la gráfica logarítmica es: ", coeficientes[0],"x +", coeficientes[1])
    
    #Representación gráfica de las cajas.
       
    #Dimensiones de la zona de las cajas y de la imagen.
    xmin, xmax = 0, img.shape[1]
    ymin, ymax = 0, img.shape[0]
    
    contador=0
    
    for dim in dimensiones:
        
        print("Representación gráfica del conteo de cajas de ", dim, "pixeles")
        
        #Creamos una figura con una cierta dimensión 
        fig, ax = plt.subplots(figsize=(10*len(dimensiones),5*len(dimensiones)))
        
        #Creamos un conjunto de subtramas, es decir, un conjunto de imágenes (1 por dimensión de la caja).
        #De no hacerlo, solo imprime por salida la última imagen
        ax = plt.subplot(1, len(dimensiones), contador+1 )

        """
        matplotlib.pyplot.imshow():  Muestra una imagen en 2D. Para ilustrar una imagen es escala de 
        grises tenemos que configurar los parámetros cmap='gray', vmin=0 y vmax=1. Donde vmin y vmax
        representan el rango que cubre el mapa de colores. 'Extend' delimita el tamaño de la imagen, es útil
        para el correcto posicionamiento de las cajas.
        https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
        """
        ax.imshow(1.0-img, cmap='gray', vmin=0, vmax=1,
                  extent=[xmin, xmax, ymin, ymax])
        
        #Quitamos los ejes de las imágenes
        ax.set_axis_off()
         
        #Dada una matríz de píxeles de tamaño img.shape[0] x img.shape[1], calcumos la suma por bloques de dim x dim 
        #Ejercicio 65 de : https://pythonworld.ru/numpy/100-exercises.html
        img_reducida=np.add.reduceat(np.add.reduceat(img, np.arange(0, img.shape[0], dim), axis=0),np.arange(0, img.shape[1], dim), axis=1)
        
        #Recorremos los píxeles de la imagen en bloques.
        for i in range (img_reducida.shape[0]):
            for j in range (img_reducida.shape[1]):
                #Comprobamos si el color se encuentra entre el blanco y negro
                if img_reducida[i][j] >0 and img_reducida[i][j] < dim*dim:
                    #En cuyo caso, creamos un rectángulo con la herramienta matplotlib.patches y lo añadimos a la figura. Es importante el buen
                    #posicionamiento de este
                     rect = patches.Rectangle( (j*dim, img.shape[0]-(i+1)*dim), width=dim, height=dim, edgecolor='0.15',facecolor='0.5', alpha=0.5)
                     ax.add_patch(rect) 
        plt.show()
        contador+=1
        
        
    return coeficientes[0]


fractal_img=RGB_To_BinaryGray(pl.imread("Imagenes/BoxCountingDimension/CantorSet9.png"))
print("La dimensión boxcounting del conjunto de Cantor es ", BoxCountingDimension(fractal_img))

fractal_img=RGB_To_BinaryGray(pl.imread("Imagenes/BoxCountingDimension/KochCurve8.png"))
print("La dimensión box counting de la curva de Koch es ", BoxCountingDimension(fractal_img))

fractal_img=RGB_To_BinaryGray(pl.imread("Imagenes/BoxCountingDimension/Sierpinski.png"))
print("La dimensión box counting del triangulo de Sierpinski es ", BoxCountingDimension(fractal_img))

fractal_img=RGB_To_BinaryGray(pl.imread("Imagenes/BoxCountingDimension/KochSquare5.png"))
print("La dimensión box counting del cuadrado de Koch es ", BoxCountingDimension(fractal_img))

fractal_img=RGB_To_BinaryGray(pl.imread("Imagenes/BoxCountingDimension/HilbertCurve.png"))
print("La dimensión box counting de la curva de Hilbert es ", BoxCountingDimension(fractal_img))



 