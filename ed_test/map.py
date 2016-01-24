import pygame
from pygame.locals import *
import sys
import random

#Constants#
MAPHEIGHT = 16
TILESIZE = 32
MAPWIDTH = 26

DIRT = 0
GRASS = 1
STONE = 3
WATER = 4
SAND = 5
WOOD = 6

TREE_DENSITY = 10

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




colors = {
        DIRT: pygame.image.load('assets/dirt.png'),
        GRASS: pygame.image.load('assets/grass.png'),
        WATER: pygame.image.load('assets/water.png'),
        STONE: pygame.image.load('assets/stone.png'),
        SAND: pygame.image.load('assets/sand.png'),
        WOOD: pygame.image.load('assets/wood.png')
        }

playerPos = [0,0]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
PLAYER = pygame.image.load('assets/player.png').convert_alpha()
TREE = pygame.image.load('assets/tree.png').convert_alpha()
DISPLAYED_TREES = False
TREE_LOCATIONS = []

for i in range(MAPHEIGHT):
    for j in range(MAPWIDTH):
        if tilemap[i][j] == 1:
            DISPLAYSURF.blit(TREE, (2, 0)) 
            if random.randrange(100) > TREE_DENSITY:
                #DISPLAYSURF.blit(TREE, (0, 0))#
                pass

for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
        if tilemap[row][column] != 1:
            print "boo"
            if random.randrange(100) < TREE_DENSITY:
                #TREE_LOCATIONS.append([row, column])#
                DISPLAYSURF.blit(TREE, (row*TILESIZE, column*TILESIZE))
pygame.display.update()


            


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
            elif (event.key == K_DOWN) and ((playerPos[1] + 1) < MAPHEIGHT and
                    tilemap[playerPos[0]][playerPos[1] + 1] != 4):
                playerPos[1] += 1
            elif (event.key == K_UP) and ((playerPos[1] - 1) >= 0):
                playerPos[1] -= 1

            print tilemap

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(colors[tilemap[row][column]],
                        (column*TILESIZE, row*TILESIZE))
                DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILESIZE,
                    playerPos[1]*TILESIZE))
                '''
                if [row, column] in TREE_LOCATIONS:
                    DISPLAYSURF.blit(TREE, (row*TILESIZE, column*TILESIZE))
                    '''


        pygame.display.update()
