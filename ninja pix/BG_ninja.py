import pygame
pygame.init()

class Background:
    
    def __init__(self,game):
        self.game = game #permet de recuperer tous ce qui a dans la class de Game, car quand on fait l instance de Background dans la class game on met self(game) en argument
        
        #recupere les dimensions de l ecran
        self.w = self.game.screen.get_width()  
        self.h = self.game.screen.get_height()
        
        #atributs avec chaque image de layer en double et redimentioné et choisi une position et une vitesse pour chacune de ces images
        self.layer1 = pygame.image.load('assets/bg/day/1.png') #calque 1
        self.layer1 = pygame.transform.scale_by(self.layer1, 2) #redimensionnement
        self.overlap1 = pygame.image.load('assets/bg/day/1.png') #double du calque 1
        self.overlap1 = pygame.transform.scale_by(self.overlap1, 2) #redimensionnement
        
        self.l1Pos = 0 #position x de calque 1
        self.o1Pos = -self.w #position x du double de calque 1
        self.speed1 = 0.5 #vitesse
        
        
        self.layer2 = pygame.image.load('assets/bg/day/2.png') #etc...
        self.layer2 = pygame.transform.scale_by(self.layer2, 2)
        self.overlap2 = pygame.image.load('assets/bg/day/2.png')
        self.overlap2 = pygame.transform.scale_by(self.overlap2, 2)
        
        self.l2Pos = 0
        self.o2Pos = -self.w
        self.speed2 = 1.0
        
        
        self.layer3 = pygame.image.load('assets/bg/day/3.png')
        self.layer3 = pygame.transform.scale_by(self.layer3, 2)
        self.overlap3 = pygame.image.load('assets/bg/day/3.png')
        self.overlap3 = pygame.transform.scale_by(self.overlap3, 2)
        
        self.l3Pos = 0
        self.o3Pos = -self.w
        self.speed3 = 2.0
        
        
        self.layer4 = pygame.image.load('assets/bg/day/4.png')
        self.layer4 = pygame.transform.scale_by(self.layer4, 2)
        self.overlap4 = pygame.image.load('assets/bg/day/4.png')
        self.overlap4 = pygame.transform.scale_by(self.overlap4, 2)
        
        self.l4Pos = 0
        self.o4Pos = -self.w
        self.speed4 = 4.0
        
        #creation de differents tableau avec chacune des valeurs
        self.layers = [self.layer1, self.layer2, self.layer3, self.layer4] #calques 
        self.overlaps = [self.overlap1, self.overlap2, self.overlap3, self.overlap4] #double des calques
        self.LPos = [self.l1Pos, self.l2Pos, self.l3Pos, self.l4Pos] #position x des calques 
        self.OPos = [self.o1Pos ,self.o2Pos, self.o3Pos, self.o4Pos] #position x du double des calques 
        self.speeds =[self.speed1, self.speed2, self.speed3, self.speed4] #vitesse
    
    #methode pour afficher les differents calques et double sur l ecran    
    def show_bg(self): 
        for i in range(4):
            self.game.screen.blit(self.layers[i], (self.LPos[i],0))
            self.game.screen.blit(self.overlaps[i], (self.OPos[i],0))
    
    #methode pour bouger le background et faire l effet parralax      
    def move_bg(self):
        for i in range(4):

            if self.game.player.last_direction == 'droite': #si le joueur va a droite
                self.LPos[i] -= self.speeds[i]
                self.OPos[i] -= self.speeds[i]

                if self.LPos[i] + self.w <= 0:
                    self.LPos[i] = self.OPos[i] + self.w
                if self.OPos[i] + self.w <= 0: 
                    self.OPos[i] = self.LPos[i] + self.w

            elif self.game.player.last_direction == 'gauche': #si le joueur va a gauche
                self.LPos[i] += self.speeds[i]
                self.OPos[i] += self.speeds[i]
                
                if self.LPos[i] >= self.w: 
                    self.LPos[i] = self.OPos[i] - self.w
                if self.OPos[i] >= self.w:
                    self.OPos[i] = self.LPos[i] - self.w

                
            
            
        
        
        