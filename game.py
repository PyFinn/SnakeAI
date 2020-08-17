import pygame
pygame.init()
pygame.display.set_caption('PyFinn Snake Game')
disp = pygame.display.set_mode((495,880))
pygame.display.update()
game_ended = False
while not game_ended:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_ended = True
 
pygame.quit()