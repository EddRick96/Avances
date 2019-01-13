#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
from time import clock
from pygame.constants import K_UP 
from pip._internal.wheel import message_about_scripts_not_on_PATH
from builtins import str

#Clases importadas
import Util
import Personajes
# variables globales
global segundos
segundos = 0
ancho = 1000
alto = 600



class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

#Creacion de botones
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=500,y=500):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else: self.imagen_actual = self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)

#Menu del Juego
def main():
    clock = pygame.time.Clock()
    tiempo=0
    tiempo2=0
    pygame.init()  # inicializo el modulo
    fuente1=pygame.font.SysFont("Arial",18,True,False)#crea la fuente
    terminar = False
    tiempo=0
    tiempo1=0    
    # fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
    pantalla = pygame.display.set_mode((700, 350))

    pygame.display.set_caption("Mi Ventana")  # Titulo de la Ventana
    # creo un reloj para controlar los fps
    reloj1 = pygame.time.Clock()

    inicio1=pygame.image.load("inicio1.png")
    inicio2 = pygame.image.load("inicio2.png")
    salir1 = pygame.image.load("salir1.png")
    salir2 = pygame.image.load("salir2.png")
    #DETENER SONIDO


    fondo = pygame.image.load("fondo.jpg")
    #SONIDO

    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(3)

    # Ubicacion del boton
    boton1 =  Boton(inicio1,inicio2,150,290)
    boton3 = Boton(salir1,salir2,350, 290)


    cursor1=Cursor()



    salir = False
    # LOOP PRINCIPAL
    while salir != True:
        tiempo+=1
        if tiempo==60:
            tiempo1+=1
            tiempo=0
        time = clock.tick(60)
        # recorro todos los eventos producidos
        # en realidad es una lista
        for event in pygame.event.get():
             if event.type==pygame.MOUSEBUTTONDOWN:

                if cursor1.colliderect(boton1.rect):

                    Inicio()

                if cursor1.colliderect(boton3.rect):
                    salir = True
            # pygame.QUIT( cruz de la ventana)
        if event.type == pygame.QUIT:
                salir = True

        if terminar==False:
            segundosint= tiempo2 #toma el tiempo que se esta ejecutando el juego
            segundos=str(segundosint)#los combierte de numero a string
            transcurre=fuente1.render("TIEMPO: "+segundos,0,pygame.Color('orange'))#pone el tiempo en un texto
        else:
            transcurre=fuente1.render("TIEMPO: "+segundos,0,pygame.Color('orange'))

        reloj1.tick(20)  # operacion para que todo corra a 20fps
        pantalla.blit(fondo,(0,0))
        cursor1.update()
        boton1.update(pantalla,cursor1)
        
        boton3.update(pantalla, cursor1)


        pygame.display.update()  # actualizo el display

    pygame.quit()

#================================================================ 


#Tamaño de la pantalla
WIDTH = 1200
HEIGHT = 500
# Constantes & Variables
ventana=pygame.display.set_mode((WIDTH,HEIGHT))

#===============================================
#inicializa las variables a ocupar durante el juego 

def Initialize():
   
    global screen, clock
   
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sonic Game")
    clock = pygame.time.Clock()
   
    return
#===============================================
#esta funcion se encarga de cargar imagenes, sonidos, musica, etc.
def LoadContent():
      
    global fondo, sonic, nivel  
   
    sonic = Personajes.Sonic()
    
   
    fondo = Util.imagen("imagen1.png")
    sonic = imagen("Sonic1.png", True)   
    sonic_inv = pygame.transform.flip(sonic, True, False)
   
    return
#===============================================
#Se encarga de detectar los cambios en el teclado y posicion de los persoanjes
def Updates():
    global sonic
    
    Util.teclado(sonic)    
    #Escenario
    #sprite_S()  
    #Enemigo()
    #Coliciones()
   
    return
#===============================================
#Cambios y movimiento del personaje
def Draw():
   
    global time
   
   
    screen.blit(fondo, (0, 0))
       
    if sonic._salto==False:
        
        if sonic._direc==True:
            screen.blit(sonic.imagenSonic(),(sonic._posX,sonic._posY))
        else:
            sonic_inv=pygame.transform.flip(sonic.imagenSonic(),True,False);
            screen.blit(sonic_inv,(sonic._posX,sonic._posY))
    else:        
        sonic.saltar()
        if sonic._direc==True:
            screen.blit(sonic._images[4],(sonic._posX,sonic._posY))
        else:
            sonic_inv=pygame.transform.flip(sonic._images[4],True,False);
            screen.blit(sonic_inv,(sonic._posX,sonic._posY))   
    
    #============================================== 
             
   
    pygame.display.flip()
   
    return

#===================================================

#================================================

#Tiempo de ejecucion del juego 
pygame.init()
#Definicmos una fuente para el tipo de letra
Fuente = pygame.font.SysFont('Arial',30)

def Inicio():
    aux=1
   
    Initialize()
   
    LoadContent()
       
    while True:
        #Creacion de una variable tiempo que se utiliza get_ticks
        #que nos da el tiempo en mili segundos
        Tiempo= pygame.time.get_ticks()/1000
        #Controla el numero de impreciones del tiempo
        if Tiempo == aux:
            aux +=1
            print (Tiempo)
        #Se crea el texto sobre el tiempo lo cual se lo combierte en str
        contador= Fuente.render('Tiempo : '+str(Tiempo),0,(30,40,0))
        #Indicamos la posicion del cronometro
        ventana.blit(contador,(120,30))


        pygame.display.update() 
        time = clock.tick(60)
       
        Updates()
       
        Draw()
       
       
       
        #if gameOver==True
            #UnLoadContent()
         
     
   
    return
 


 
if __name__ == '__main__': 
    main()
