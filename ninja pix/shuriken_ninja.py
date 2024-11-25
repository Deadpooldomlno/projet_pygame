import pygame
pygame.init()

class Shuriken(pygame.sprite.Sprite): #class Shuriken qui est un sprite
    
    def __init__(self,player):
        super().__init__() #constructeur du sprite
        self.player = player #permet de recuperer tous ce qui a dans la class de Player, car quand on fait l instance de Shuriken dans la class Player on met self(player) en argument
        
        #recupere les dimensions de l ecran
        self.w = self.player.w 
        self.h = self.player.h
        
        self.image = pygame.image.load('assets/shuriken.png') #image
        self.image = pygame.transform.scale_by(self.image, 3) #redimensionnement de l image
        self.rect = self.image.get_rect() #recupere la surface
        self.rect.x = self.player.rect.x + 40 #correspond au point en haut a gauche sur l axe x, qui varrie selon la position du joueur
        self.rect.y = self.player.rect.y + 60 #mem chose mais sur l axe y 

        self.speed = 12
        self.angle = 0
        self.origin_image = self.image
        
        self.direction = self.player.last_direction
        
    #methode pour fait tourner le shuriken en fonction de la direction du joueur
    def rotate(self):
        if self.direction == 'droite':
            self.angle -= 12
        elif self.direction == 'gauche':
            self.angle += 12
            
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
        
    
    #methode pour faire avancre le shuriken
    def move(self):
        if self.direction == 'droite':
            self.rect.x += self.speed
        elif self.direction == 'gauche':
            self.rect.x -= self.speed
            
        self.rotate() #appelle de l amethode rotate
            
        if self.rect.x <= 0 or self.rect.x >= self.w:
            self.remove()
    
    #methode pour supprimer un sprite du groupe de sprite
    def remove(self):
        self.player.all_shoots.remove(self)
        #print('suppr')

