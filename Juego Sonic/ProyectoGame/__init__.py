#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 1200
HEIGHT = 800
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
    
    sonic_camina[0]=(0,0,32,40)
    sonic_camina[1]=(196,2,236,40)
    sonic_camina[2]=(240,2,280,40)
    sonic_camina[3]=(283,1,308,40)
    sonic_camina[4]=(312,2,351,40)
    sonic_camina[5]=(0,0,32,40)
    
    Rsonic_camina[0]=(0,0,32,40)
    Rsonic_camina[1]=(196,2,236,40)
    Rsonic_camina[2]=(240,2,280,40)
    Rsonic_camina[3]=(283,1,308,40)
    Rsonic_camina[4]=(312,2,351,40)
    Rsonic_camina[5]=(0,0,32,40)

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
    
    fondo=imagen("Imagenes/ppz-2-present.png").convert()
    
    
    sonic=imagen("Imagenes/sprite-sonic.png", True)
    sonic_inv=pygame.transform.flip(sonic, True, False)
    
    reloj=pygame.time.Clock()
    
    #fondo=pygame.transform.rotozoom(fondo, (1000, 400))
    
                 
    #Bucle principal del juego 
    while True:
        
        time = reloj.tick(60)
        
        sprite()
        teclado()
        
        
        
        screen.blit(fondo,(-288,0))
        if direc==True:
            screen.blit(sonic, ( MposX, 368),(sonic_camina[i]))
   
        if direc==False:
            screen.blit(sonic_inv, ( MposX, 368),(Rsonic_camina[i]))
           
    
        pygame.display.flip()
        
        #Cerrar la ventana
        
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
    return 0
 
if __name__ == '__main__':
    
    main()
#=====================================================