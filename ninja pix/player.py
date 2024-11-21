import pygame
pygame.init()

w,h = 1280,720

class Player():
    
    #constructeur
    def __init__(self,game):
        
        self.speed_x = 10
        self.jump_strenght = -10
        self.g = 0.5 
        self.speed_y = 0  
        self.jumping = False

        
        self.moving = False
        
        self.img_idleD = [pygame.image.load(f'assets/idle{i}D.png') for i in range(1,3)]      #liste avec chaque image de idle
        self.img_idleD = [pygame.transform.scale_by(img, 8) for img in self.img_idleD]        #redimentionne la taille de l image 
        
        self.img_idleG = [pygame.image.load(f'assets/idle{i}G.png') for i in range(1,3)]  
        self.img_idleG = [pygame.transform.scale_by(img, 8) for img in self.img_idleG]  
        
        self.img_runD = [pygame.image.load(f'assets/run{i}D.png') for i in range(1,7)]        #liste avec chaque image de run
        self.img_runD = [pygame.transform.scale_by(img, 8) for img in self.img_runD]
        
        self.img_runG = [pygame.image.load(f'assets/run{i}G.png') for i in range(1,7)]    
        self.img_runG = [pygame.transform.scale_by(img, 8) for img in self.img_runG]
        
        self.img_jumpD = pygame.image.load('assets/jumpD.png')
        self.img_jumpD = pygame.transform.scale_by(self.img_jumpD, 8)
        
        self.img_jumpG = pygame.image.load('assets/jumpG.png')
        self.img_jumpG = pygame.transform.scale_by(self.img_jumpG, 8)
        
        
        self.current_image = self.img_idleD[0]
        self.image_index = 0
        self.animation_speed = 0.07
        self.rect = self.current_image.get_rect(center= (w/2,h-134))
        
        
       
    #methode pour ce deplacer          
    def move(self):
        
        self.moving = False
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT] and self.rect.left >=0:           #deplace a gauche
            self.rect.x -= self.speed_x
            self.moving = True
        if pressed[pygame.K_RIGHT] and self.rect.right <=w:         #deplace a droite
            self.rect.x += self.speed_x
            self.moving = True
            
        
        if self.jumping:
            self.speed_y += self.g  
            self.rect.y += self.speed_y
            
            
            if self.rect.bottom >= h - 70:
                self.rect.bottom = h - 70
                self.jumping = False
                self.velocity_y = 0
        
        self.update_animation()
                
    def jump(self):
        if not self.jumping: 
            self.jumping = True
            self.speed_y = self.jump_strenght
        self.update_animation()
    
    
    #methode de l animation de player       
    def update_animation(self):
                
        if self.moving:
            image = self.img_runD
        elif self.jumping:
            image = self.img_jumpD        
        else:
            image = self.img_idleD

        if image == self.img_runD:
            self.image_index += self.animation_speed + 0.08
            if self.image_index >= len(image):
                self.image_index = 0
            self.current_image = image[int(self.image_index)]
        
        elif image == self.img_idleD:
            self.image_index += self.animation_speed
            if self.image_index >= len(image):
                self.image_index = 0
            self.current_image = image[int(self.image_index)]

            


        
