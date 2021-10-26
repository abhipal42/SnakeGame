# Title: Basic Snake Game on Python

# Description: This is a basic snake game that was developed on python using pygame. 

# Created by: Abhinav Palisetti
# Credit: https://www.edureka.co/blog/snake-game-with-pygame/ 


import pygame as game
from characters import *
from board import *

#screen characteristics
width = 800
height = 600

#snake characteristics
black = (0, 0, 0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
square = [200,150,10,10]
snake_speed = 12
block_movement = 10

#control setup
x1 = width/2
y1 = height/2
x_change = 0
y_change = 0
game_clock = game.time.Clock()

#key controls
key_pressed = game.KEYDOWN
left = game.K_LEFT
right = game.K_RIGHT
up = game.K_UP
down = game.K_DOWN
q = game.K_q
c = game.K_c
spacebar = game.K_SPACE

#Starting the Screen
game.init()
game_display = game.display.set_mode((width,height))
game.display.update()
game.display.set_caption("Snake Game by Abhinav")

#Creating instances of object
snake1 = Snake()
apple1 = Apple()

def game_loop():

    #Game Reset Settings
    game_over = False
    game_close = False

    x1 = width/2
    y1 = height/2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    fdx, fdy = apple1.food_location(width, height, block_movement)

    #Running of Game
    while not game_close:

        while game_over:

            #Game Over Screen
            game_display.fill(white)
            message(game_display,"You Lost", red, width/2, height/2)
            my_score(game_display, snake_length - 1, blue)
            game.display.update()
            
            for event in game.event.get():
                if event.type == game.QUIT:
                    game_close = True
                    return
                if event.type == key_pressed:
                    if event.key == q:
                        game_close = True
                        return
                    elif event.key == spacebar:
                        game_loop()
                game.display.update()

        #Controlling of Snake
        for event in game.event.get():
            if event.type == game.QUIT:
                game_close = True
            x_change, y_change = controls(event, left, right, up, down, block_movement, x_change, y_change)

        #Creating Boundaries of Game
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
    
        x1 += x_change
        y1 += y_change

        #Character images are refreshed
        game_display.fill(black)
        snake1.shape(game_display,green,x1,y1,10)   
        apple1.shape(game_display, red, fdx, fdy, 10)
        game.display.update()

        #Extension of Snake every time it eats the apple
        snake1.head(snake_list,snake_length,x1,y1)
        snake1.snake_extension(game_display, green, 10, snake_list)
        my_score(game_display, snake_length - 1, blue)
        game.display.update()

        #Checks to see if snake ate apple
        if x1 == fdx and y1 == fdy:
            fdx, fdy = apple1.food_location(width, height, block_movement)
            snake_length += 1

        #Speed of Game gradually increases
        game_clock.tick(snake_speed + (snake_length -1))

    game.display.update()
    game.quit()
    quit()


game_loop()
