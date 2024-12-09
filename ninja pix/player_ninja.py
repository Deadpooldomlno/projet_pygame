from shuriken_ninja import Shuriken #importation de la class Shuriken

import pygame
pygame.init()

class Player():
    
    #constructeur
    def __init__(self,game):
        self.game = game #permet de recuperer tous ce qui a dans la class de Game, car quand on fait l instance de Player dans la class Game on met self(game) en argument

        #recupere les dimensions de l ecran
        self.w = self.game.screen.get_width() 
        self.h = self.game.screen.get_height()
         
        self.speed_x = 10 #vitesse horinzontal (a voir si on garde)
        self.speed_y = 0 #vitesse verticale
        
        self.jump_strenght = -10 #force du saut
        self.g = 0.5 #gravité
        
        self.last_direction = 'droite' #correspond au sens du joeur, droite par defaut
        self.jumping = False #est entrain de sauter ?
        self.moving = False #est entrain de se deplacer ?
        
        #attributs correspondant aux images du joueur
        self.img_idleD = [pygame.image.load(f'assets/player/idle{i}D.png') for i in range(1,3)] #liste avec chaque image de idle orienté vers la droite(quand il fait rien)    
        self.img_idleD = [pygame.transform.scale_by(img, 8) for img in self.img_idleD] #redimensionnement     
        
        self.img_idleG = [pygame.image.load(f'assets/player/idle{i}G.png') for i in range(1,3)] #meme chose mais orienté vers la gauche
        self.img_idleG = [pygame.transform.scale_by(img, 8) for img in self.img_idleG]  
        
        self.img_runD = [pygame.image.load(f'assets/player/run{i}D.png') for i in range(1,7)] #liste avec chaque image de run orienté vers la droite(quand il court) 
        self.img_runD = [pygame.transform.scale_by(img, 8) for img in self.img_runD]
        
        self.img_runG = [pygame.image.load(f'assets/player/run{i}G.png') for i in range(1,7)] #meme chose mais orienté vers la gauche
        self.img_runG = [pygame.transform.scale_by(img, 8) for img in self.img_runG]
        
        self.img_jumpD = pygame.image.load('assets/player/jumpD.png') #image de jump orienté vers le droite(quand il saute)
        self.img_jumpD = pygame.transform.scale_by(self.img_jumpD, 8)
        
        self.img_jumpG = pygame.image.load('assets/player/jumpG.png') #meme chose mais orienté vers la gauche
        self.img_jumpG = pygame.transform.scale_by(self.img_jumpG, 8)
        
        
        self.current_image = self.img_idleD[0] #image principale, idle droite par defaut
        self.image_index = 0
        self.animation_speed = 0.07 #vitesse de rotation entre chaque image
        
        self.rect = self.current_image.get_rect(center= (self.w/2,self.h-134)) #recupere la surface de l image principale, et indique son centre 
         
        self.all_shoots = pygame.sprite.Group() #groupe de sprite qui va contenir chaque instance du Shuriken
        
        self.vie= 3 #la vie du personnage
    #methode pour ce deplacer          
    def move(self):
        if not self.game.collision(self, self.all_ennemis):
            self.moving = False
            
            pressed = pygame.key.get_pressed()
            
            #deplace vers la gauche
            if pressed[pygame.K_LEFT] and self.rect.left >=0: #si fleche de gauche est pressée
                #self.rect.x -= self.speed_x (a voir si on garde)
                self.moving = True
                self.last_direction = 'gauche' #orienté vers la gauche
                self.game.bg.move_bg() #mouvement dsu bg pour donner l impresion de deplacement
            
            #meme chose mais se deplace vers la droite
            if pressed[pygame.K_RIGHT] and self.rect.right <=self.w: #si fleche de droite est pressée
                #self.rect.x += self.speed_x
                self.moving = True
                self.last_direction = 'droite'
                self.game.bg.move_bg()
                
            #si il saute
            if self.jumping:
                self.speed_y += self.g  
                self.rect.y += self.speed_y
                
                
                if self.rect.bottom >= self.h - 70:
                    self.rect.bottom = self.h - 70
                    self.jumping = False
                    self.speed_y = 0
            
            self.update_animation() #appelle de la methode pour faire changer l animation en fonction
        
        #methode de saut
    def jump(self):
        if not self.jumping: 
            self.jumping = True
            self.speed_y = self.jump_strenght
        
    
    
    #methode de l animation de player       
    def update_animation(self):
        
        pressed = pygame.key.get_pressed()
        
        #condition pour changer l image principale du joueur 
        if self.jumping: #si il saute
            if self.last_direction == 'droite':
                image = self.img_jumpD
            elif self.last_direction == 'gauche':
                image = self.img_jumpG  
        
        elif self.moving: #si deplacement horinzontale
            if pressed[pygame.K_RIGHT]:
                image = self.img_runD
            if pressed[pygame.K_LEFT]:
                image = self.img_runG
        
        else: #si il fait rien(idle)
            if self.last_direction == 'droite':
                image = self.img_idleD
            if self.last_direction == 'gauche':
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
            
    #methode pour lancer un shuriken        
    def shoot(self):
        self.all_shoots.add(Shuriken(self)) #ajoute une instance de Shuriken dans le groupe de sprite
            
