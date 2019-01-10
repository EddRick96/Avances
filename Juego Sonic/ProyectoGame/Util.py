import pygame, sys
from pygame.locals import *



def imagen(filename, transparent=False,expandir=False):
        message = 'ERROR'
        try: image = pygame.image.load(filename)
        except (pygame.error, message):
                raise (SystemExit, message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
                
        if expandir:
            image=pygame.transform.scale2x(image)
                
        return image

 
def teclado(sonic):
   
    teclado = pygame.key.get_pressed()
    
    if teclado[K_q] and sonic._salto==False:
        sonic._salto=True
        sonic._subida=True
        
    
    if teclado[K_RIGHT]:
        sonic._posX+=2
        sonic._con+=1
        sonic._direc=True
       
    elif teclado[K_LEFT]:
        sonic._posX-=2
        sonic._con+=1
        sonic._direc=False
    else:
        sonic._frame=0
    
    
    if sonic._con>=6:        
        sonic._frame+=1
        sonic._con=0
    
      
    # Cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   
       
    return
 