import pygame as game
import random

class Snake():

    def shape(self, screenName, color, blockPosition_x, blockPosition_y, size):
        game.draw.rect(screenName, color, [blockPosition_x, blockPosition_y, size, size])
    

    def head(self, snake_list, snake_length, x, y):
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
 
    def movement(self, screen, color, x, y):
        game.draw.rect(screen, color, [x,y,10,10])


    def snake_extension(self, screenName, color, snake_block, snake_list):
        for element in snake_list:
            game.draw.rect(screenName, color, [element[0], element[1], snake_block, snake_block])


class Apple():


    def shape(self, screenName, color, blockPosition_x, blockPosition_y, size):

        game.draw.rect(screenName, color, [blockPosition_x, blockPosition_y, size, size])
    
    
    def food_location(self, width, height, block_movement):
        foodx = round(random.randrange(0, width - block_movement) / 10.0) * 10.0
        foody = round(random.randrange(0, height - block_movement) / 10.0) * 10.0
        return foodx, foody



