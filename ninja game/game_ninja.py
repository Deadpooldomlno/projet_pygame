from player_ninja import Player #importation de la class Player
from BG_ninja import Background #importation de la class Background
from Ennemi import Ennemi

import pygame
pygame.init()

class Game():
    
    def __init__(self,screen):
        self.screen = screen #permet de recuperer l ecran, car quand on fait l instance de Game dans le fichier principale(main) on met screen en argument
        
        #recupere donc les dimensions de l ecran
        self.w = self.screen.get_width() 
        self.h = self.screen.get_height()
        
        self.bg = Background(self) #instance de Background avec self(donc game) en atribut
        self.player = Player(self) #instance de Player avec self(donc game) en atribut
        
        self.all_ennemis = pygame.sprite.Group() # Groupe de monstre
        
        
        self.all_players =pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.spawn_Ennemi()
    def collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group, False, pygame.sprite.collide_mask)
    
    def spawn_Ennemi(self):
        monster = Ennemi(self)
        self.all_ennemis.add(monster)
