import sys, pygame

class Sonic(object):

    _posX=62
    _posY=364
    _frame=0
    _images=[]
    _con=0
    _direc=True
    _salto=False
    _subida=True

    def __init__(self):
        tileset=pygame.image.load("Sonic1.png").convert()        
        color = tileset.get_at((0,0))
        
        tileset.set_colorkey(color)
        
        self._images.append(tileset.subsurface((2,2,27,39)))
        
        self._images.append(tileset.subsurface((30,2,25,39)))        
        
        self._images.append(tileset.subsurface((56,2,24,39)))
        
        self._images.append(tileset.subsurface((81,2,35,39)))
        
        self._images.append(tileset.subsurface((117,1,36,40)))
        
        self._images.append(tileset.subsurface((154,1,33,40)))                
        
        for i in range(len(self._images)):
            self._images[i]
     
        return 
    
    def imagenSonic(self):
        
        if self._frame==len(self._images)-1:
            self._frame=0 
        
        return self._images[self._frame]        
     
    def saltar(self):
        
        if self._subida==True:
            self._posY-=4
            if self._direc==True:
                self._posX+=1
            else:
                self._posX-=1
            
            
        if self._posY<=232:
            self._subida=False
            
            
        if self._subida==False:
            self._posY+=4            
            if self._direc==True:
                self._posX+=1
            else:
                self._posX-=1
            
        if self._subida==False and self._posY>=364:
            self._subida=True
            self._salto=False
            self._frame=0
        
            

        
        
        
    


        return  
