import pygame
#Initialize
pygame.init()

#Set Caption
pygame.display.set_caption('PyFinn Snake Game')

#Define RGB Colors
black = (0,0,0)
white = (255,255,255)


disp = pygame.display.set_mode((495,880))
pygame.display.update()
game_ended = False
while not game_ended:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_ended = True
    pygame.draw.rect(disp,white,[200,150,10,10])
    pygame.display.update()
 
pygame.quit()