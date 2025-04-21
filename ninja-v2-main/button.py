import pygame
pygame.init()

class Button:
    
    def __init__(self,screen,images,pos,scale=None):
        self.screen=screen
        self.pos = pos
        
        self.image1=pygame.image.load(images[0])
        self.image2=pygame.image.load(images[1])
        if scale:
            self.image1 = pygame.transform.scale_by(self.image1, 3)
            self.image2 = pygame.transform.scale_by(self.image2, 3)
        
        self.current_image = self.image1
        self.rect = self.current_image.get_rect(center=pos)
        
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.check_collision(mouse_pos):
            self.current_image = self.image2
        else:
            self.current_image = self.image1
        
        self.screen.blit(self.current_image,self.rect)
    
    def check_collision(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)
            
                
class Texte:
    
    def __init__(self,screen,image,pos,scale=None):
        self.screen=screen
        self.pos = pos
        self.image = pygame.image.load(image)
        if scale:
            self.image=pygame.transform.scale_by(self.image,2)
        
        self.rect = self.image.get_rect(center=pos)
        
    def draw(self):
        self.screen.blit(self.image,self.rect)
        
        
    