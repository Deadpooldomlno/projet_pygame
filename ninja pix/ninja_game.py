from player_ninja import Player

import pygame
pygame.init()

class Game():
    
    def __init__(self):
        self.player = Player(self)