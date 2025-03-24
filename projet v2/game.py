from player import Player
from ennemy import Ennemy
import pygame
pygame.init()

class Game:
    
    def __init__(self):
        self.w = 1000
        self.h = 600
        self.gravite = 0.5
        self.vitesse_max_chute = 12
        
        self.player = Player(self)
        self.ennemy = Ennemy(self,110,390,300)
    