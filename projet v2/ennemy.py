import pygame
pygame.init()
from random import randint

class Ennemy:
    
    def __init__(self,game,x1,x2,y):
        self.game = game
        self.surf = pygame.Surface((40,40))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.rect.x = x1
        self.rect.y = y
        
        
        self.x1 = x1
        self.x2 = x2
        
        self.vx = 0 
        self.vy = 0
        self.vitesse_deplacement = 2
    
    def deplacer_gauche(self):
        self.vx = -self.vitesse_deplacement 
        
    def deplacer_droite(self):
        self.vx = self.vitesse_deplacement 
    
    def degat(self):
        pass

    def update(self,plateformes,players):
        if self.rect.x <= self.x2:
            self.deplacer_droite()
        #if self.rect.x >= self.x1:
            #self.deplacer_gauche()
            
        
        self.vy += self.game.gravite
        self.vy = min(self.vy, self.game.vitesse_max_chute)

        self.rect.x += self.vx
        
        #detection horizontale ennemi - plateforme
        for plateforme in plateformes:
            if self.rect.colliderect(plateforme):
                if self.vx > 0:
                    self.rect.right = plateforme.left
                    self.deplacer_gauche()
                elif self.vx < 0:  
                    self.rect.left = plateforme.right
                    self.deplacer_droite()
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.deplacer_droite()
        elif self.rect.right > self.game.w:
            self.rect.right = self.game.w
            self.deplacer_gauche()
        
        self.rect.y += self.vy
        
        rect_test = self.rect.copy()
        rect_test.y += 1
        
        #detection verticale ennemi - plateforme
        for plateforme in plateformes:
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

        #detection horizontale ennemi - joueur
        for player in players:
            if self.rect.colliderect(player):
                if self.vx > 0:
                    self.rect.right = player.left
                if self.vx < 0:  
                    self.rect.left = player.right
