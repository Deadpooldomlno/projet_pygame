import pygame
pygame.init()
from random import randint

class Slime:
    
    def __init__(self,game,pos,range):
        self.game = game
        
        self.g = pygame.image.load('assets/slimeG.png')
        self.g = pygame.transform.scale_by(self.g,1.5)
        
        self.d = pygame.image.load('assets/slimeD.png')
        self.d = pygame.transform.scale_by(self.d,1.5)
        
        self.current_image = self.d
        
        self.rect = self.current_image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
        self.start_x = pos[0]
        self.range = range
        
        self.vitesse_deplacement = 2
        self.direction = 1
        self.vx = 0 
        self.vy = 0

    def update(self):
        self.animation()
        
        self.vy += self.game.gravite
        self.vy = min(self.vy, self.game.vitesse_max_chute)
        
        if self.rect.x > self.start_x + self.range:
            self.direction = -1

        elif self.rect.x < self.start_x:
            self.direction = 1

        self.vx = self.vitesse_deplacement * self.direction
        
        self.rect.x += self.vx
        
        #detection horizontale ennemi - plateforme
        for plateforme in self.game.plateformes:
            if self.rect.colliderect(plateforme):
                if self.vx > 0:
                    self.rect.right = plateforme.left
                    self.vx = -self.vitesse_deplacement
                elif self.vx < 0:  
                    self.rect.left = plateforme.right
                    self.vx = self.vitesse_deplacement
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = self.vitesse_deplacement
        elif self.rect.right > self.game.w:
            self.rect.right = self.game.w
            self.vx = -self.vitesse_deplacement
        
        self.rect.y += self.vy
        
        rect_test = self.rect.copy()
        rect_test.y += 1
        
        #detection verticale ennemi - plateforme
        for plateforme in self.game.plateformes:
            if self.rect.colliderect(plateforme) or rect_test.colliderect(plateforme):
                if self.vy > 0: 
                    self.rect.bottom = plateforme.top
                    self.vy = 0 
                elif self.vy < 0: 
                    self.rect.top = plateforme.bottom
                    self.vy = self.game.gravite +2
        
        if self.rect.bottom +1 > self.game.h:
            self.rect.bottom = self.game.h
            self.vy = 0             
        elif self.rect.top < 0:
            self.rect.top = 0
            self.vy = self.game.gravite +2
            
    def animation(self):
        if self.direction >0:
            self.current_image = self.d
        else:
            self.current_image = self.g
            
    def draw(self):
        self.game.screen.blit(self.current_image, self.rect)