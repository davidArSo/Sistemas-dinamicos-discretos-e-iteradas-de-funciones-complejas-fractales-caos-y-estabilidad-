#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 4 19:08:38 2021

@author: David Armenteros Soto
"""
"""
4 FRACTALES 
    4.2 Sistema de Lindenmayer
       
El presente programa sirve de apoyo a la sección 4.2 en la que se explica que 
son los sistemas de Lindenmayer y que utilidad tienen a la hora de construir fractales
mediantes unas reglas de producción.
"""

import turtle

#Clase para los sistemas de Lindenmayer
class LSystem:
    
    def __init__(self,axioma,reglas,longitud,theta):
        """
        Constructor de la clase  
    
        Parámetros
        ----------
        axioma: Axioma del sistema-L
        reglas: reglas de producción del sistema-L
        longitud: longitud del paso
        theta: ángulo de giro
        """ 
        self.axioma=axioma
        self.reglas=reglas
        self.longitud=longitud
        self.theta=theta
     
    def generate_word(self,iteraciones,palabra):
        """
        Genera la palabra final, asociada al fractal en una determinada iteración.
        Comienza por el axioma y aplica sucesivamente las distintas reglas.
    
        Parámetros
        ----------
        iteraciones: iteraciones que se llevarán a cabo
        palabra: palabra con la que comenzamos
        
        Returns
        -------
        Palabra final, trás aplicar las reglas de producción.
        """ 
        
        #Si el número de iteraciones es 0, devolvemos el axioma
        if iteraciones == 0:
            return palabra
        #En otro caso, aplicamos las reglas para obtener la palabra final
        else:
            palabra_final=''
            #Recorremos todos los caracteres de la palabra
            for caracter in list (palabra):
                #Si al carácter hay que aplicarle una regla, modificamos la palabra final
                #con la regla
                if caracter in self.reglas:
                    palabra_final+=self.reglas[caracter]
                #En caso contrario el carácter se queda como está
                else:
                    palabra_final+=caracter
            #Aplicamos recursividad, para realizar este proceso tantas veces como
            #iteraciones queramos 
            return self.generate_word(iteraciones-1,palabra_final)
 
    
    def draw_lsystem(self,iteraciones):
        """
        Define los comandos e interpreta la palabra final para construir el fractal
    
        Parámetros
        ----------
        iteraciones: iteraciones que se llevarán a cabo
        """
        
        #Pila para ramificaciones
        stack=[]
        
        #Generamos la palabra final
        palabra_final=self.generate_word(iteraciones, self.axioma)
            
        #Recorremos la palabra y aplicamos una interpretación gráfica de 
        #los comandos
        for comando in list(palabra_final):   
            turtle.pendown()
            
            if comando =="F":
                turtle.forward(self.longitud)
            elif comando =="f":
                turtle.penup()
                turtle.forward(self.longitud)
            elif comando == "+":
                turtle.left(self.theta)
            elif comando == "-":
                turtle.right(self.theta)
            elif comando == "L":
                turtle.left(self.theta)
                turtle.forward(self.longitud)
                turtle.right(self.theta)
                turtle.forward(self.longitud)
                turtle.right(self.theta)
                turtle.forward(self.longitud)
                turtle.left(self.theta)
            elif comando == "R":
                turtle.right(self.theta)
                turtle.forward(self.longitud)
                turtle.left(self.theta)
                turtle.forward(self.longitud)
                turtle.left(self.theta)
                turtle.forward(self.longitud)
                turtle.right(self.theta)
            elif comando == "S":
                turtle.forward(self.longitud)
                turtle.left(self.theta)
                turtle.forward(self.longitud)
                turtle.left(self.theta)
                turtle.forward(self.longitud)
                turtle.right(self.theta)
                turtle.forward(self.longitud)
                turtle.right(self.theta)
                turtle.forward(self.longitud)
            elif comando == "D":
                turtle.right(self.theta)
                turtle.right(self.theta)
                turtle.forward(self.longitud)
                turtle.left(self.theta)
                turtle.left(self.theta)
                turtle.forward(self.longitud)
            elif comando == "E":
                turtle.forward(self.longitud)
                turtle.right(self.theta)
                turtle.right(self.theta)
                turtle.forward(self.longitud)
                turtle.left(self.theta)
                turtle.left(self.theta)
            #Almacenamos el estado actual en la parte superior de la pila (posición, dirección)
            elif comando == "[":
                stack.append((turtle.position(), turtle.heading()) )
            #Eliminamos el tope de la pila y nos dirigimos a esa posición 
            elif comando == "]":
                turtle.penup()
                position, heading =stack.pop()
                turtle.goto(position)
                turtle.setheading(heading)
                turtle.pendown()
 
def start_drawing():
    """
    Define el punto y la dirección de inicio de la tortuga
    """
    turtle.clear()
    turtle.penup()
    turtle.goto(-350,-100)
    turtle.pendown() 
    turtle.setheading(0.0)
  
      
if __name__ == '__main__':
    
    
    #Definición de los siguientes sistemas de Lindenmayer:
    kochCurve=LSystem('F', 
                 {'F': 'F+F--F+F' , '+': '+' , '-': '-'  }, 
                 5,
                 60,
                 )
    
    CantorSet=LSystem('F', 
                 {'F': 'FfF' , 'f': 'fff' ,   }, 
                 3,
                 0,
                 )
    
    SierpinskiArrowHead=LSystem('L', 
                 {'L': '+R-L-R+' , 'R': '-L+R+L-', '+': '+' , '-': '-'  }, 
                 3,
                 60,
                 )
    PeanoCurve=LSystem('F', 
                 {'F': 'FF+F+F+FF+F+F-F' , '+': '+' , '-': '-'  }, 
                 50,
                 90,
                 )
    DragonCurve=LSystem('D', 
                 {'D': '-D++E' , 'E': 'D--E+', '+': '+' , '-': '-'  }, 
                 10,
                 45,
                 )
    HilbertCurve=LSystem('L', 
                 {'L': '+RF-LFL-FR+' , 'R': '-LF+RFR+FL-', 'F':'F', '+': '+' , '-': '-'  }, 
                 20,
                 90,
                 )
    RegularWeed=LSystem('F', 
                 {'F': 'F[+F]F[-F]F' }, 
                 10,
                 25.7,
                 )
    SimpleBush=LSystem('F', 
                 {'F': 'FF+[+F-F-F]-[-F+F+F]' }, 
                 10,
                 25,
                 )
    
    turtle.speed('fastest')
    turtle.ht()
    start_drawing()
    
    turtle.title("La curva de Koch mediante un sistema-L")
    iteracion=4
    palabra_final=kochCurve.generate_word(iteracion, kochCurve.axioma)
    print("La palabra que genera la curva de Koch en la iteración ", iteracion, " es: ", palabra_final)
    kochCurve.draw_lsystem(iteracion)
  
    start_drawing()
 
    turtle.title("El conjunto de Cantor mediante un sistema-L")
    iteracion=5
    palabra_final=CantorSet.generate_word(iteracion, CantorSet.axioma)
    print("La palabra que genera el conjunto de Cantor en la iteración ", iteracion, " es: ", palabra_final)
    CantorSet.draw_lsystem(iteracion)
 
    
    start_drawing()
    
    turtle.title("La punta de flecha de Sierpinski mediante un sistema-L")
    iteracion=6
    palabra_final=SierpinskiArrowHead.generate_word(iteracion, SierpinskiArrowHead.axioma)
    print("La palabra que genera la curva de la punta de flecha de Sierpinski en la iteración ", iteracion, " es: ", palabra_final)
    SierpinskiArrowHead.draw_lsystem(iteracion)
    turtle.ht()
    
    start_drawing()
    turtle.title("La curva del dragón mediante un sistema-L")
    
    iteracion=6
    palabra_final=DragonCurve.generate_word(iteracion, DragonCurve.axioma)
    print("La palabra que genera la curva del dragón en la iteración ", iteracion, " es: ", palabra_final)
    DragonCurve.draw_lsystem(iteracion)
    turtle.ht()
  
    
    start_drawing()
    turtle.title("La curva de Peano mediante un sistema-L")
    
    iteracion=2
    palabra_final=PeanoCurve.generate_word(iteracion, PeanoCurve.axioma)
    print("La palabra que genera la curva de Peano en la iteración ", iteracion, " es: ", palabra_final)
    PeanoCurve.draw_lsystem(iteracion)
    turtle.ht()
    
    start_drawing()
    turtle.title("La curva de Hilbert mediante un sistema-L")
    
    iteracion=4
    palabra_final=HilbertCurve.generate_word(iteracion, HilbertCurve.axioma)
    print("La palabra que genera la curva de Hilbert en la iteración ", iteracion, " es: ", palabra_final)
    HilbertCurve.draw_lsystem(iteracion)
    turtle.ht() 
    
   
    turtle.setheading(90)
    start_drawing()
    turtle.title("Ramificación de la maleza mediante un sistema-L")
   
    iteracion=3
    palabra_final=RegularWeed.generate_word(iteracion, RegularWeed.axioma)
    print("La palabra que genera la maleza en la iteración ", iteracion, " es: ", palabra_final)
    RegularWeed.draw_lsystem(iteracion)
    turtle.ht()
   
    turtle.setheading(90)
    start_drawing()
    turtle.title("Ramificaciones de un arbusto mediante un sistema-L")
     
    iteracion=3
    palabra_final=SimpleBush.generate_word(iteracion, SimpleBush.axioma)
    print("La palabra que genera el arbusto en la iteración ", iteracion, " es: ", palabra_final)
    SimpleBush.draw_lsystem(iteracion)
    turtle.ht()
    
    turtle.bye()
   