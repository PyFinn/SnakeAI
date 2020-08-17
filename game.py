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

#Define Font
score_font = pygame.font.SysFont("comicsansms", 35)

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
    snake_length = 0
    last_cords = []
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
        snake_cords = []
        x_old = x
        y_old = y
        last_cords.append([x_old, y_old])
        x += x_new
        y += y_new
        disp.fill(black)
        pygame.draw.rect(disp,white,[x,y,10,10])
        for number in range(snake_length):
            number += 1
            x_cord = last_cords[-(number)][0]
            y_cord = last_cords[-(number)][1]
            pygame.draw.rect(disp,white,[x_cord, y_cord,10,10])
            snake_cords.append([x_cord, y_cord])
        pygame.draw.rect(disp,green,[food_cords[0],food_cords[1],10,10])
        value = score_font.render("Score: " + str(snake_length), True, green)
        disp.blit(value, [0, 0])
        pygame.display.update()
        for cords in snake_cords:
            if cords[0] == x and cords[1] == y:
                game_ended = True
        if (x == food_cords[0] and y == food_cords[1]):
            food_cords = spawn_food(495, 880)
            snake_length += 1
        timer.tick(30)
 
pygame.quit()