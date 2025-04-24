from game import Game
import pygame
pygame.init()

w,h=1000,600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('ninja')
pygame.display.set_icon(pygame.image.load('assets/icon2.png'))

game = Game(screen)

fps= pygame.time.Clock()

#main
def main():
    state = 'menu' 
    pass_state ='menu'
    
    while state != 'quit':
        if state == 'play':
            state = play()
            pass_state ='play'
        
        elif state == 'setting':
            state = setting(pass_state)
            pass_state ='setting'
        
        elif state == 'menu':
            state = menu()
            pass_state ='menu'
            
        elif state == 'restart':
            if pass_state == 'menu':
                game.nb_mort = 0
            game.reset()
            state = 'play'
            pass_state ='restart'

    pygame.quit()

#jeu
def play():    
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.player.sauter()
                if event.key == pygame.K_DOWN:
                    game.player.tp()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if game.button_setting.check_collision(mouse_pos):
                        return 'setting'
                    if game.button_restart.check_collision(mouse_pos):
                        game.nb_mort +=1
                        return 'restart'
                
        k = pygame.key.get_pressed()
        
        if k[pygame.K_LEFT] and k[pygame.K_RIGHT]:
            game.player.arreter()
        if k[pygame.K_LEFT]:
            game.player.deplacer_gauche()
        elif k[pygame.K_RIGHT]:
            game.player.deplacer_droite()
        else:
            game.player.arreter()
        
        screen.fill((255,255,255))
        
        for plateforme in game.plateformes:
            pygame.draw.rect(screen, (0,0,0), plateforme)
        
        for portal in game.portals:
            portal.draw()
        
        game.player.draw()
        game.player.update()
        
        for slime in game.slimes:
            slime.draw()
            slime.update()

        for spike in game.spikes:
            spike.draw()
        
        game.draw_bande_grise()
        for button in [game.button_setting,game.button_restart]:
            button.draw()
        
        game.draw_text('death: '+str(game.nb_mort),(270,9))
        game.draw_text('timer: 00:00:00',(15,9))
        
        pygame.display.update()

#options  
def setting(pass_state):
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if game.button_quit.check_collision(mouse_pos):
                        return 'quit'
                    if game.button_menu.check_collision(mouse_pos):
                        return 'menu'
                    if game.button_play.check_collision(mouse_pos):
                        return 'play'
        
        screen.fill((255,255,255))
        game.draw_bande_grise()
        for button in [game.button_play,game.button_menu,game.button_quit]:
            button.draw()
        
        if pass_state == 'play':
            game.draw_text('timer: 00:00:00',(15,9))
        else:
            game.draw_text('best time: 00:00:00',(15,9))
            

        pygame.display.update()
#menu      
def menu():
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if game.button_play.check_collision(mouse_pos):
                        return 'restart'
                    if game.button_setting.check_collision(mouse_pos):
                        return 'setting'
        
        screen.fill((255,255,255))
        game.draw_bande_grise()
        for button in [game.button_play,game.button_setting]:
            button.draw()
        
        game.draw_text('best time: 00:00:00',(15,9))
        
        pygame.display.update()

main()