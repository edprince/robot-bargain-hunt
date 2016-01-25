import pygame
from pygame.locals import *
import sys
import random

#Constants#
FPS = 30
#Map data#
MAPHEIGHT = 20
TILESIZE = 32
MAPWIDTH = 26
TREE_DENSITY = 20
#Tiles#
DIRT = 0
GRASS = 1
STONE = 3
WATER = 4
SAND = 5
WOOD = 6


tilemap = []
i = 0


def read_file(f):
    file_object = open(f, 'r')
    return file_object.read()

def parse_map(data):
    tilemap_tmp = []
    '''
    types = {
            '#': GRASS,
            '~': WATER,
            'v': SAND,
            '_': STONE,
            '"': DIRT,
            '=': WOOD
            }
    rows = data.split('/')
    return [[types.get(tile, -1) for tile in row] for row in rows]
    '''
    for line in data:
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


parse_map(read_file('map_data.txt'))


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
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
#Load more assets
PLAYER = pygame.image.load('assets/player.png').convert_alpha()
TREE = pygame.image.load('assets/tree.png').convert_alpha()
TREE_LOCATIONS = []

for i in range(MAPHEIGHT):
    for j in range(MAPWIDTH):
        DISPLAYSURF.blit(TREE, (2, 0)) 
        r = random.randrange(100)
        if r > TREE_DENSITY:
            #DISPLAYSURF.blit(TREE, (0, 0))#
            print r 
            pass

for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
        if tilemap[row][column] == 1:
            if random.randrange(100) < TREE_DENSITY:
                TREE_LOCATIONS.append([row, column])#
                #DISPLAYSURF.blit(TREE, (row*TILESIZE, column*TILESIZE))
                #pygame.display.update()


            


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
            print (playerPos[0], playerPos[1])


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


    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            if [row, column] in TREE_LOCATIONS:
                DISPLAYSURF.blit(TREE, (column*TILESIZE, row*TILESIZE))
    pygame.display.update()
    FPSCLOCK.tick()
