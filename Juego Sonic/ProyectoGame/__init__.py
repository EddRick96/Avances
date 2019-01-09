#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from time import clock
from pygame.constants import K_UP 

#Tamaño de la pantalla
WIDTH = 1200
HEIGHT = 500
# Constantes & Variables
SposX = 62
SposY = 364

cont=6
direc=True
i=0

bajada = False

salto = False
salto_Par = False

#===============================================

def Initialize():
   
    global screen, clock,sonic_camina,Rsonic_camina
   
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sonic Game")
    clock = pygame.time.Clock()
   
    sonic_camina={}
    Rsonic_camina={}
   
    sonic_camina[0]=(1,0,29,41)
    sonic_camina[1]=(29,0,54,41)
    sonic_camina[2]=(56,0,80,41)
    sonic_camina[3]=(80,0,116,41)
    sonic_camina[4]=(116,0,153,41)
    sonic_camina[5]=(153,0,32,41)
    
    Rsonic_camina[0]=(482,1,511,41)
    Rsonic_camina[1]=(456,1,482,41)
    Rsonic_camina[2]=(431,1,456,41)
    Rsonic_camina[3]=(395,0,431,41)
    Rsonic_camina[4]=(358,0,395,41)
    Rsonic_camina[5]=(324,0,358,41)
   
    return
#===============================================
def LoadContent():
   
    global fondo, sonic,sonic_inv  
   
    fondo = imagen("Imagenes/stage1_vacio.png").convert()
    sonic = imagen("Imagenes/Sonic1.png", True)
    sonic_inv = pygame.transform.flip(sonic, True, False)
   
    return
#===============================================
def Updates():
   
    teclado()    
    #Escenario
    sprite_S()  
    #Enemigo()
    #Coliciones()
   
    return
#===============================================
def Draw():
   
    global salto,salto_Par, salto,bajada_Par,bajada
   
   
    screen.blit(fondo, (0, 0))
       
       
    global SposX, SposY
       
    if direc==True and salto==False :
        screen.blit(sonic, ( SposX, SposY),(sonic_camina[i]))
   
    if direc==False and salto==False :
        screen.blit(sonic_inv, ( SposX, SposY),(Rsonic_camina[i]))
       
       
#salto normal y Parabolico
    if salto==True:            
            if direc==True:
                screen.blit(sonic, ( SposX, SposY),(sonic_camina[4]))
            if direc==False:
                screen.blit(sonic_inv, ( SposX, SposY),(Rsonic_camina[4]))  
           
            if bajada==False:
                SposY-=4              
               
            if bajada==True:
                SposY+=4              
           
            if SposY<=232:
                bajada=True
           
            if SposY>=364:
                bajada=False
                salto=False
#============================================== 
             
   
    pygame.display.flip()
   
    return
#=================IMAGEN========================
def imagen(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except (pygame.error, message):
        raise (SystemExit, message)
    image = image.convert()
    if transparent :
        color= image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

#============TECLADO=============================
def teclado():
    
    global SposX
    global cont, direc, salto
    
    teclado = pygame.key.get_pressed()
   
    if teclado[K_UP]:
        salto=True
       
    if teclado[K_RIGHT]:
        SposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]:
        SposX-=2
        cont+=1
        direc=False            
    else :
        cont=6
         
   
    # Cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   
         
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