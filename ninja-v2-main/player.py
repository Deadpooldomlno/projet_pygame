import pygame
pygame.init()

class Player():
    
    def __init__(self,game):
        self.game = game
        
        self.last_direction = 1 #correspond au sens du joeur, droite par defaut
        
        #attributs correspondant aux images du joueur
        self.img_idleD = [pygame.image.load(f'assets/player/idle{i}D.png') for i in range(1,3)] #liste avec chaque image de idle orientée vers la droite(quand il fait rien)    
        self.img_idleD = [pygame.transform.scale_by(img, 5) for img in self.img_idleD] #redimensionnement     
        
        self.img_idleG = [pygame.image.load(f'assets/player/idle{i}G.png') for i in range(1,3)] #meme chose mais orientée vers la gauche
        self.img_idleG = [pygame.transform.scale_by(img, 5) for img in self.img_idleG]  
        
        self.img_runD = [pygame.image.load(f'assets/player/run{i}D.png') for i in range(1,7)]
        self.img_runD = [pygame.transform.scale_by(img, 5) for img in self.img_runD]
        
        self.img_runG = [pygame.image.load(f'assets/player/run{i}G.png') for i in range(1,7)]
        self.img_runG = [pygame.transform.scale_by(img, 5) for img in self.img_runG]
        
        self.img_jumpD = pygame.image.load('assets/player/jumpD.png')
        self.img_jumpD = pygame.transform.scale_by(self.img_jumpD, 5)
        
        self.img_jumpG = pygame.image.load('assets/player/jumpG.png')
        self.img_jumpG = pygame.transform.scale_by(self.img_jumpG, 5)
        
        
        self.current_image = self.img_idleD[0] #image principale, idle droite par defaut
        self.image_index = 0
        self.animation_speed = 0.07 #vitesse de rotation entre chaque image
        
        self.rect = self.current_image.get_rect(center= (950,100)) #recupere la surface de l image principale, et indique son centre 
        self.vx = 0 
        self.vy = 0
        
        self.peut_sauter = False
        
        self.vitesse_deplacement  = 4
        self.force_saut = -9
        
    def deplacer_gauche(self):
        self.vx = -self.vitesse_deplacement 
        
    def deplacer_droite(self):
        self.vx = self.vitesse_deplacement 
        
    def arreter(self):
        self.vx = 0
        
    def sauter(self):
        if self.peut_sauter:
            self.vy = self.force_saut
        
    def update(self):
        self.animation()
        
        self.vy += self.game.gravite
        self.vy = min(self.vy, self.game.vitesse_max_chute)
        
        if self.vx>0:
            self.last_direction = 1
        elif self.vx<0:
            self.last_direction = -1
        
        self.rect.x += self.vx
        
        #detection horizontale joueur - plateforme
        for plateforme in self.game.plateformes:
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
        for plateforme in self.game.plateformes:
            if self.rect.colliderect(plateforme) or rect_test.colliderect(plateforme):
                if self.vy > 0: 
                    self.rect.bottom = plateforme.top
                    self.vy = 0 
                    self.peut_sauter = True
                elif self.vy < 0: 
                    self.rect.top = plateforme.bottom
                    self.vy = self.game.gravite +0.5
        
        if self.rect.bottom +1 > self.game.h:
            self.rect.bottom = self.game.h
            self.vy = 0
            self.peut_sauter = True               
        elif self.rect.top < 40:
            self.rect.top = 40
            self.vy = self.game.gravite +0.5
        
        #detection collisions joueur - spikes
        for spike in self.game.spikes:
            if self.rect.colliderect(spike.rect):
                self.game.nb_mort+=1
                self.game.reset()
                
        
        #detection joueur - slimes
        for slime in self.game.slimes:
            if self.rect.colliderect(slime):
                if self.vy > 0 and self.rect.bottom - self.vy <= slime.rect.top:
                    self.rect.bottom = slime.rect.top
                    self.vy = -self.vy
                else:
                    if self.vx > 0:
                        self.rect.right = slime.rect.left
                    elif self.vx < 0:
                        self.rect.left = slime.rect.right
                    self.vy = 0
                    self.arreter()
                    self.game.nb_mort+=1
                    self.game.reset()
        
    def tp(self):
        for portal in self.game.portals:
            if self.rect.colliderect(portal.rect1):
                self.rect.center = portal.rect2.center
                self.arreter()
                self.vy = 0
            
            elif self.rect.colliderect(portal.rect2):
                self.rect.center = portal.rect1.center
                self.arreter()
                self.vy = 0
                
    
    def animation(self):
        #condition pour changer l image principale du joueur 
        if not self.peut_sauter: #si il est en l'air
            if self.last_direction == 1:
                image = self.img_jumpD
            elif self.last_direction == -1:
                image = self.img_jumpG  
        
        elif self.vx!=0: #si deplacement horinzontale
            if self.vx>0:
                image = self.img_runD
            if self.vx<0:
                image = self.img_runG
        
        else: #si il fait rien(idle)
            if self.last_direction == 1:
                image = self.img_idleD
            if self.last_direction == -1:
                image = self.img_idleG

        #condition pour regler correctement l animation
        if image == self.img_jumpD or image == self.img_jumpG:
            self.current_image = image
        
        elif image == self.img_runD or image == self.img_runG:
            self.image_index += self.animation_speed + 0.08
            if self.image_index >= len(image):
                self.image_index = 0
            self.current_image = image[int(self.image_index)]
        
        elif image == self.img_idleD or image == self.img_idleG:
            self.image_index += self.animation_speed
            if self.image_index >= len(image):
                self.image_index = 0
            self.current_image = image[int(self.image_index)]
            
    def draw(self):
        self.game.screen.blit(self.current_image, self.rect)
                                        

        
