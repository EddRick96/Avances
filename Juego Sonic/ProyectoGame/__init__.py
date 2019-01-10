#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
from time import clock
import os
from ProyectoGame import Personajes
from ProyectoGame import Escenario
from ProyectoGame import Util


#Tamaño de la pantalla
WIDTH = 1200
HEIGHT = 500

#===============================================
#inicializa las variables a ocupar durante el juego 

def Initialize():
   
    global screen, clock,sonic_camina,Rsonic_camina
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sonic Game")
    clock = pygame.time.Clock()
   
    
   
    return screen
#===============================================
#esta funcion se encarga de cargar imagenes, sonidos, musica, etc.
def LoadContent():
   
    global fondo, sonic, nivel  
   
    sonic = Personajes.Sonic()
    
    nivel= Escenario.Mapa()
    
    nivel.cargarMapa("Nivel0")
    #fondo = imagen("Imagenes/stage1_vacio.png").convert()
    #sonic = imagen("Imagenes/SonicSprite.png", True)
    #sonic_inv = pygame.transform.flip(sonic, True, False)
   
    return
#===============================================
#Se encarga de detectar los cambios en el teclado y posicion de los persoanjes
def Updates():
    global sonic
    
    Util.teclado(sonic)
    #teclado()    
    #Escenario
    #sprite_S()  
    #Enemigo()
    #Coliciones()
   
    return
#===============================================
#Cambios y movimiento del personaje
def Draw():
    
    global time
     
    screen.blit(fondo,(0,0) )
        
    for i in range(nivel._MapaH ):
        for j in range(nivel._MapaW):
            
            pos=nivel._matrizMapa[i][j]
            screen.blit(nivel._mapaImagenes[pos-1],(j*32,i*32) )
            

        
   
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
        
            
        
            
    
       
    pygame.display.flip()
   
   
         
    return
#===================================================
#=============SPRITE================================
def sprite_S():
    
    global cont
    p=6
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if cont==p*5:
        i=4
   
    if cont==p*6:
        i=5
        cont=0
   
    return

#================================================ 
def main():
   
    Initialize()
   
    LoadContent()
   
    global time   
    
    
    while True:
       
        time = clock.tick(60)
       
        Updates()
       
        Draw()
       
       
       
        #if gameOver==True
            #UnLoadContent()
         
     
   
    return
 
if __name__ == '__main__':
    
    main()
#=====================================================