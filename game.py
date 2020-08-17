import pygame

#Initialize
pygame.init()

#Set Caption
pygame.display.set_caption('PyFinn Snake Game')

#Define RGB Colors
black = (0,0,0)
white = (255,255,255)

#Set and Update the Dissplay
disp = pygame.display.set_mode((495,880))
pygame.display.update()

game_ended = False

x = 200
y = 150

x_new = 0
y_new = 0

timer = pygame.time.Clock()

while not game_ended:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_ended = True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                x_new = -10
                y_new = 0
            elif event.key == pygame.K_RIGHT:
                x_new = 10
                y_new = 0
            elif event.key == pygame.K_UP:
                x_new = 0
                y_new = -10
            elif event.key == pygame.K_DOWN:
                x_new = 0
                y_new = 10
    x += x_new
    y += y_new
    disp.fill(black)
    pygame.draw.rect(disp,white,[x,y,10,10])
    pygame.display.update()
    timer.tick(30)
 
pygame.quit()