import pygame as game

def message(screenName, msg, color, x, y):
    input = game.font.SysFont(None, 50).render(msg, True, color)
    screenName.blit(input, [x, y])


def my_score(screenName, score, color):
    message(screenName, "Score: " + str(score), color, 0, 0)


def controls(iteration, left, right, up, down, movement, currentX, currentY):

    changeOfX = currentX
    changeOfY = currentY

    if iteration.type == game.KEYDOWN:
        if iteration.key == left:
            changeOfX = -movement
            changeOfY = 0
        elif iteration.key == right:
            changeOfX = movement
            changeOfY = 0
        elif iteration.key == up:
            changeOfX = 0
            changeOfY = -movement
        elif iteration.key == down:
            changeOfX = 0
            changeOfY = movement

    return changeOfX, changeOfY