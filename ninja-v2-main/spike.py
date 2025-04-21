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