import pygame
pygame.init()

class Player():
    
    def __init__(self,game):
        self.game = game
        
        self.surf = pygame.Surface((40,40))
        self.surf.fill((0,0,255))
        self.rect = self.surf.get_rect(center = (self.game.w/2,self.game.h/2))
        
        self.vx = 0 
        self.vy = 0
        
        self.peut_sauter = False
        
        self.vitesse_deplacement  = 5
        self.force_saut = -10
        
    def deplacer_gauche(self):
        self.vx = -self.vitesse_deplacement 
        
    def deplacer_droite(self):
        self.vx = self.vitesse_deplacement 
        
    def arreter(self):
        self.vx = 0
        
    def sauter(self):
        if self.peut_sauter:
            self.vy = self.force_saut

        
    def update(self,plateformes,ennemies):
        self.vy += self.game.gravite
        self.vy = min(self.vy, self.game.vitesse_max_chute)

        self.rect.x += self.vx
        
        #detection horizontale joueur - plateforme
        for plateforme in plateformes:
            if self.rect.colliderect(plateforme):
                if self.vx > 0:
                    self.rect.right = plateforme.left
                elif self.vx < 0:  
                    self.rect.left = plateforme.right
                self.arreter()
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.arreter()
        elif self.rect.right > self.game.w:
            self.rect.right = self.game.w
            self.arreter()
        
        self.rect.y += self.vy
        
        self.peut_sauter = False
        
        rect_test = self.rect.copy()
        rect_test.y += 1
        
        #detection verticale joueur - plateforme
        for plateforme in plateformes:
            if self.rect.colliderect(plateforme) or rect_test.colliderect(plateforme):
                if self.vy > 0: 
                    self.rect.bottom = plateforme.top
                    self.vy = 0 
                    self.peut_sauter = True
                elif self.vy < 0: 
                    self.rect.top = plateforme.bottom
                    self.vy = self.game.gravite +2
        
        if self.rect.bottom +1 > self.game.h:
            self.rect.bottom = self.game.h
            self.vy = 0
            self.peut_sauter = True               
        elif self.rect.top < 0:
            self.rect.top = 0
            self.vy = self.game.gravite +2
        
        #detection horizontale joueur - ennemi
        for ennemy in ennemies:
            if self.rect.colliderect(ennemy):
                if self.vx > 0:
                    self.rect.right = ennemy.left
                elif self.vx < 0:  
                    self.rect.left = ennemy.right
                    
        #detection verticale joueur - ennemi
        for ennemy in ennemies:
            if self.rect.colliderect(ennemy) or rect_test.colliderect(ennemy):
                if self.vy > 0: 
                    self.vy = 0
                                        

        

