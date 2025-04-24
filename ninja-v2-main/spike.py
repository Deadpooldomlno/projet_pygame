import pygame
pygame.init()

class Spike:
    
    def __init__(self,screen,pos,nb):
        self.screen = screen
        if nb ==1:
            self.image= pygame.image.load('assets/spike.png')
        else:
            self.image= pygame.image.load('assets/spike2.png')
            
        self.rect=self.image.get_rect(center=pos)
        
    def draw(self):
        self.screen.blit(self.image,self.rect)


class Portal:
    
    def __init__(self,screen,pos1,pos2):
        self.screen=screen
        
        self.image1=pygame.image.load('assets/portal1.png')
        self.image1=pygame.transform.scale_by(self.image1,4)
        self.rect1 =self.image1.get_rect(center=pos1)
        
        self.image2=pygame.image.load('assets/portal2.png')
        self.image2=pygame.transform.scale_by(self.image2,4)
        self.rect2 =self.image2.get_rect(center=pos2)
        
    def draw(self):
        self.screen.blit(self.image1,self.rect1)
        self.screen.blit(self.image2,self.rect2)
        
        
    