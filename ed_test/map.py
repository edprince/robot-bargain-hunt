import pygame
from pygame.locals import *
import sys

DIRT = 0
GRASS = 1
STONE = 3
WATER = 4
SAND = 5
WOOD = 6

file_object = open('map_data.txt', 'r')
map_data = file_object.read()
tilemap_tmp = []
tilemap = []
i = 0
for line in map_data:
    if line == '#':
        tilemap_tmp.append(GRASS)
    elif line == '~':
        tilemap_tmp.append(WATER)
    elif line == 'v':
        tilemap_tmp.append(SAND)
    elif line == '_':
        tilemap_tmp.append(STONE)
    elif line == '"':
        tilemap_tmp.append(DIRT)
    elif line == '=':
        tilemap_tmp.append(WOOD)
    elif line == '/':
        tilemap.append(tilemap_tmp)
        tilemap_tmp = []


BROWN = (153, 76, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


colors = {
        DIRT: pygame.image.load('assets/dirt.png'),
        GRASS: pygame.image.load('assets/grass.png'),
        WATER: pygame.image.load('assets/water.png'),
        STONE: pygame.image.load('assets/stone.png'),
        SAND: pygame.image.load('assets/sand.png'),
        WOOD: pygame.image.load('assets/wood.png')
        }
TILESIZE = 32
MAPWIDTH = 26
MAPHEIGHT = 16

playerPos = [0,0]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
PLAYER = pygame.image.load('assets/player.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and ((playerPos[0] + 1) < MAPWIDTH):
                playerPos[0] += 1
            elif (event.key == K_LEFT) and ((playerPos[0] - 1) >= 0):
                playerPos[0] -= 1
            elif (event.key == K_DOWN) and ((playerPos[1] + 1) < MAPHEIGHT):
                playerPos[1] += 1
            elif (event.key == K_UP) and ((playerPos[1] - 1) >= 0):
                playerPos[1] -= 1

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(colors[tilemap[row][column]],
                        (column*TILESIZE, row*TILESIZE))
                DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILESIZE,
                    playerPos[1]*TILESIZE))

        pygame.display.update()
