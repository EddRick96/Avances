#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes & Variables
WIDTH = 1200
HEIGHT = 500
SposX = 62
SposY = 364

cont=6
direc=True
i=0
sonic_camina={}
Rsonic_camina={}

parabola={}
salto = False
salto_Par = False
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
    global cont, direc, salto, salto_Par
    
    teclado=pygame.key.get_pressed()
    
   
    if teclado[K_UP] and teclado[K_RIGHT] and salto_Par==False:
        salto_Par=True
    elif teclado[K_UP] and teclado[K_LEFT] and salto_Par==False:
        salto_Par=True
         
    elif teclado[K_RIGHT]and salto==False and salto_Par==False:
        SposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]and salto==False and salto_Par==False:
        SposX-=2
        cont+=1
        direc=False
    elif teclado[K_UP] and salto==False and salto_Par==False:
        salto=True          
    else :
        cont=6
   
       
       
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
    

    
    global salto_Par
    bajada = False
    bajada_Par = False             
    #Bucle principal del juego 
    while True:
          
        time = reloj.tick(60)     
        sprite()
        teclado()
       
        
        screen.blit(fondo,(0,0))
        
        global SposX, SposY, salto
        
        if direc==True:
            screen.blit(sonic, ( SposX, SposY),(sonic_camina[i]))
   
        if direc==False:
            screen.blit(sonic_inv, ( SposX, SposY),(Rsonic_camina[i]))
           
        #Salto Normal
        if salto==True:            
           
            if direc==True:
                screen.blit(sonic, ( SposX, SposY),(sonic_camina[4]))
            if direc==False:
                screen.blit(sonic_inv, ( SposX, SposY),(Rsonic_camina[4]))  
           
            if bajada==False:
                SposY-=4              
               
            if bajada==True:
                SposY+=4              
           
            if SposY==232:
                bajada=True
           
            if SposY==364:
                bajada=False
                salto=False
        #======================================  
       
        #SALTO PARABOLICO
        if salto_Par==True and direc==True:            
           
            screen.blit(sonic, ( SposX, SposY),(sonic_camina[4]))
           
            if bajada_Par==False:
                SposY-=3
                SposX+=2
               
            if bajada_Par==True:
                SposY+=3
                SposX+=2
           
            if SposY==292:
                bajada_Par=True
           
            if SposY==364:
                bajada_Par=False
                salto_Par=False
        elif salto_Par==True and direc==False:            
           
            screen.blit(sonic_inv, ( SposX, SposY),(Rsonic_camina[4]))
           
            if bajada_Par==False:
                SposY-=3
                SposX-=2
               
            if bajada_Par==True:
                SposY+=3
                SposX-=2
           
            if SposY==292:
                bajada_Par=True
           
            if SposY==364:
                bajada_Par=False
                salto_Par=False  
        
        pygame.display.flip()
        
        #Cerrar la ventana
        
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
    return 0
 
if __name__ == '__main__':
    
    main()
#=====================================================