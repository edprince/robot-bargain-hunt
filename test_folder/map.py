#import pygame
#from pygame.locals import *
from PIL import Image

image = Image.open('assets/wood.png')
image.show()

tilemap = [
        [GRASS, STONE, WATER],
        [WATER, WATER, WATER],
        [GRASS, WATER, WATER],
        [STONE, GRASS, GRASS],
        [STONE, GRASS, GRASS]
        ]

BROWN = (153, 76, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
STONE = 3
WATER = 4

colors = {
        DIRT: BROWN,
        GRASS: GREEN,
        WATER: BLUE,
        STONE: BLACK
        }
TILESIZE = 100
MAPWIDTH = 3
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]],
                        (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

        pygame.display.update()
