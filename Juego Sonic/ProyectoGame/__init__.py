#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 1200
HEIGHT = 500
MposX = 62

cont=6
direc=True
i=0
sonic_camina={}
Rsonic_camina={}
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
    teclado=pygame.key.get_pressed()
    
    global MposX
    global cont, direc
   
       
    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]:
        MposX-=2
        cont+=1
        direc=False
    elif teclado[K_UP]:
        #SALTO
        MposX-=2
       
    return
#===================================================
#=============SPRITE=============================
def sprite():
    global cont
    
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
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sonic Game")
    
    fondo=imagen("Imagenes/stage1_vacio.png").convert()
    
    
    sonic=imagen("Imagenes/Sonic1.png", True)
    sonic_inv=pygame.transform.flip(sonic, True, False)
    
    reloj=pygame.time.Clock()
    
    #fondo=pygame.transform.rotozoom(fondo, (1000, 400))
    
                 
    #Bucle principal del juego 
    while True:
        
        time = reloj.tick(60)
        
        sprite()
        teclado()
        
        
        screen.blit(fondo,(0,0))
        if direc==True:
            screen.blit(sonic, ( MposX, 364),(sonic_camina[i]))
   
        if direc==False:
            screen.blit(sonic_inv, ( MposX, 364),(Rsonic_camina[i]))
           
    
        pygame.display.flip()
        
        #Cerrar la ventana
        
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
    return 0
 
if __name__ == '__main__':
    
    main()
#=====================================================