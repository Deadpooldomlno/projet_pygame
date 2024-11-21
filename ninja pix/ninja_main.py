from ninja_game import Game

import pygame
pygame.init()

     
w,h = 1280,720
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('ninja pix')

#fond, pas definitif
ciel = pygame.Surface((w,h))
ciel.fill((66, 175, 250))
sol = pygame.Surface((w,70))
sol.fill((86, 101, 115))


game = Game()

FPS = pygame.time.Clock()
running = True
#boucle principale
while running:
    
    #dessine l arriere plan
    screen.blit(ciel, (0,0))
    screen.blit(sol, (0,h-70))
    #dessine le jour sur lecran
    screen.blit(game.player.current_image, game.player.rect)
    
    game.player.move()
    #print(game.player.moving)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.player.jump()

    pygame.display.flip()
    FPS.tick(60)
pygame.quit()