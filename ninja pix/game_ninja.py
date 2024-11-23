from player_ninja import Player #imortation de la class Player
from BG_ninja import Background #imortation de la class Background


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
        
        
 
        