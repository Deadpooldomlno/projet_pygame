from button import *
from spike import *
from player import Player
from slime import Slime
import pygame
pygame.init()

class Game:
    
    def __init__(self,screen):
        self.screen=screen
        self.w = screen.get_width()
        self.h = screen.get_height()
        self.gravite = 0.5
        self.vitesse_max_chute = 12      
        
        self.nb_mort =0
        
        self.player = Player(self)
        self.players=[]
        self.players.append(self.player)
        
        self.plateformes = [pygame.Rect(20, 186, 130, 10),pygame.Rect(330, 186, 10, 10),pygame.Rect(520, 186, 10, 10),
                            pygame.Rect(710, 186, 10, 10),pygame.Rect(900, 186, 50, 10),pygame.Rect(20, 346, 130, 10),
                            pygame.Rect(500, 500, 300, 10)
                            ]
        
        self.portals=[Portal(screen,(71,278),(925,118))]
       
           
        self.slimes = []

        self.spikes=[Spike(screen,(136,208),2),Spike(screen,(136,334),1)]

        
        #boutons
        self.button_setting = Button(screen,('assets/buttons/setting1.png','assets/buttons/setting2.png'),(self.w-30,20))
        self.button_restart = Button(screen,('assets/buttons/restart1.png','assets/buttons/restart2.png'),(self.w-66,20))
        self.button_play = Button(screen,('assets/buttons/play1.png','assets/buttons/play2.png'),(self.w/2,self.h/2),True)
        self.button_menu = Button(screen,('assets/buttons/menu1.png','assets/buttons/menu2.png'),(self.w/2,self.h/2-90),True)
        self.button_quit = Button(screen,('assets/buttons/exit1.png','assets/buttons/exit2.png'),(self.w/2,self.h/2+90),True)

    #dessine du texte
    def draw_text(self,str,pos):
        font = pygame.font.SysFont('Consolas',25)
        text = font.render(str,True,(255,255,255))
        rect =text.get_rect()
        rect.x =pos[0]
        rect.y =pos[1]
        self.screen.blit(text,rect)
    
    #desine une bande grise
    def draw_bande_grise(self):
        surf = pygame.Surface((self.w,40))
        surf.fill((127,127,127))
        surf_rect=surf.get_rect()
        self.screen.blit(surf,surf_rect)
    
    #reinitialise le jeu
    def reset(self):
        self.player = Player(self)
        self.players=[]
        self.players.append(self.player)
   
        self.slimes = []

        