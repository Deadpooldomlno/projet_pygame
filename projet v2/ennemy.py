import pygame
pygame.init()

class Ennemy:
    
    def __init__(self,game,x,y,d):
        self.game = game
        self.surf = pygame.Surface((40,40))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.d = d
        self.depart_x = x
        self.depart_y = y
        self.pv = 100
        self.damage = 25
        self.vx = 0
        self.vy = 0
        self.vitesse_deplacement  = 5
        self.direction = 1
        
    def update(self,d):
        self.vy += self.game.gravite
        self.vy = min(self.vy, self.game.vitesse_max_chute)
        
        self.rect.x += self.vx
        
        if self.rect.x < self.rect.x + self.d:
            self.vx += self.vitesse_deplacement
        else:
            self.direction = -self.direction
        
        if self.rect.x > self.depart_x:
            self.vx += self.vitesse_deplacement
        else:
            self.direction = -self.direction
            
        
        """
        self.vx += self.vitesse_deplacement * self.direction
        if self.direction<0:
            if self.rect.x <= self.depart_x:
                self.direction = -self.direction
        else:
            if self.rect.x >= self.rect.x+d:
                self.direction = -self.direction
        """
        
        
        
        