from game_ninja import Game #importation de la class Game

import pygame #importatio de pygame
pygame.init() #initialisation de pyagme

     
w,h = 1152,718
screen = pygame.display.set_mode((w,h)) #on defini la taille de la fenetre
pygame.display.set_caption('ninja pix') #on choi un nom

#sol pas definitif
sol = pygame.Surface((w,70))
sol.fill((86, 101, 115))


game = Game(screen) #instanciation de Game avec screen en argument

FPS = pygame.time.Clock() 
running = True

#boucle principale
while running:
    
    #affiche le sol et le background
    game.bg.show_bg()
    screen.blit(sol, (0,h-70))
      
    screen.blit(game.player.current_image, game.player.rect) #affiche le joueur sur l ecran
    game.player.move() #methode pour fair avancer le joeur

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #condition pour fermer la fenetre
            running = False
        if event.type == pygame.KEYDOWN: #si une touche et pressée
            if event.key == pygame.K_UP: #saute si fleche du haut est pressée
                game.player.jump()

    pygame.display.flip() #met ajoeur la fenetre
    FPS.tick(60) #60 images par seconde
pygame.quit() #fermeture de pygame