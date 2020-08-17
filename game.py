import pygame
import random

#Initialize
pygame.init()

#Set Caption
pygame.display.set_caption('PyFinn Snake Game')

#Define RGB Colors
black = (0,0,0)
white = (255,255,255)
green = (124,252,0)

#Set and Update the Dissplay
disp = pygame.display.set_mode((495,880))
pygame.display.update()

#Spawn random food
def spawn_food(max_x, max_y):
    foodx = round(random.randrange(0, max_x - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, max_y - 10) / 10.0) * 10.0
    return foodx, foody

game_closed = False

timer = pygame.time.Clock()

while not game_closed:
    game_ended = False
    x = 200
    y = 150

    x_new = 0
    y_new = 0

    food_cords = spawn_food(495, 880)
    while not game_ended:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                game_ended = True
                game_closed = True
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
        if (x >= 495 or x <= 0 or y >= 880 or y <=0):
            game_ended = True
        x += x_new
        y += y_new
        disp.fill(black)
        pygame.draw.rect(disp,white,[x,y,10,10])
        pygame.draw.rect(disp,green,[food_cords[0],food_cords[1],10,10])
        pygame.display.update()
        if (x == food_cords[0] and y == food_cords[1]):
            food_cords = spawn_food(495, 880)
        timer.tick(30)
 
pygame.quit()