##############################
# Marco Tulio Montoya Angulo #
# - - - - A01254155  - - - - #
##############################

#################
# I M P O R T S #
#################

import pygame
import random
import time

from pygame.locals import *

# Declare game map
mazeMap = [
    '1111111111111111111',
    '1 1               1',
    '1 1 111 1 111111111',
    '1   1   1         1',
    '1 111 111111111 1 1',
    '1 1   1       1 1 1',
    '1 11111 11111 111 1',
    '1   1       1 1   1',
    '111 1 11111 1 1 1 1',
    '1   1 1   1 1 1 1 1',
    '111 1 1 1 1 1 1 1 1',
    '1   1   1 1 1   1 1',
    '1 1111111 111111111',
    '1       1 1       1',
    '11111 1 1 1 11111 1',
    '1   1 1 1   1   1 1',
    '1 111 1 11111 1 1 1',
    '1     1       1 1 1',
    '1111111111111111111',

]


###############
# P L A Y E R #
###############

class Player:

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single(dx, 0)
        if dy != 0:
            self.move_single(0, dy)

    def move_single(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
            if self.rect.colliderect(end):

                globals()['playing'] = False
                globals()['win'] = True
                return


###########
# W A L L #
###########
class Wall:

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)


pygame.init()

black = (0, 0, 0)
green = (0, 255, 0)
DISPLAYSURF = pygame.display.set_mode((570, 570))
pygame.display.set_caption("Hello world!")


# Declare middle of DISPLAYSURF
xScreen = yScreen = 570 // 2
font = pygame.font.Font('freesansbold.ttf', 32)  # Define font and font style

step = 1

walls = []
clock = pygame.time.Clock()

x, y = 0, 0

for row in mazeMap:
    for column in row:
        if column == "1":
            Wall((x, y))
        x += 30
    y += 30
    x = 0

player = Player()

playing = True
win = False

while playing:
    DISPLAYSURF.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    # Detect keys
    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_LEFT]:
        player.move(-step, 0)
    if key_input[pygame.K_RIGHT]:
        player.move(step, 0)
    if key_input[pygame.K_UP]:
        player.move(0, -step)
    if key_input[pygame.K_DOWN]:
        player.move(0, step)

    DISPLAYSURF.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(DISPLAYSURF, (random.randint(120, 255), 0, 0), wall.rect)

    end = pygame.draw.rect(DISPLAYSURF, (0, random.randint(120, 255), 0), pygame.Rect(510, 510, 30, 30))

    pygame.draw.rect(DISPLAYSURF, (0, random.randint(120, 255), random.randint(100, 255)), player.rect)

    pygame.display.flip()
    clock.tick(360)

################
# END MESSAGES #
################
if win:
    text = font.render('You Won!', True, green, black)  # Declare text and styles
    textRect = text.get_rect()
    textRect.center = (xScreen, yScreen)

    DISPLAYSURF.fill(black)

    DISPLAYSURF.blit(text, textRect)

    pygame.display.flip()
    time.sleep(2)

textEnd = font.render('Thanks for playing', True, green, black)
textRectEnd = textEnd.get_rect()
textRectEnd.center = (xScreen, yScreen)

DISPLAYSURF.fill(black)
DISPLAYSURF.blit(textEnd, textRectEnd)
pygame.display.flip()

time.sleep(2)

# Quit game
pygame.quit()

#########
# E N D #
#########
