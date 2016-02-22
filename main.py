#Current ouput should be the list of items in descending order

from functions import *
from classes import *
import pygame
from pygame.locals import *
import sys
import math
import random
#import psyco 
#psyco.full()
objs = [] 


def calculate_distance(x1, y1, x2, y2):
    width = math.sqrt((x2 - x1)**2)
    height = math.sqrt((y2 - y1)**2)
    return math.sqrt(height**2 + width**2)

WIDTH = 50
HEIGHT = 30
TILESIZE = 32
BLUE = (0, 0, 255)
TIME = 30
#Initialize items

item_1 = pygame.image.load('assets/crown.png')
item_2 = pygame.image.load('assets/crown.png')
item_3 = pygame.image.load('assets/crown.png')
item_4 = pygame.image.load('assets/crown.png')
item_5 = pygame.image.load('assets/crown.png')

SAND = pygame.image.load('assets/sand.png')


game_items = {    
    item_1: Item('coin', 2, (10, 10), 'treasure', 10),
    item_2: Item('crown', 200, (14, 1), 'treasure', 2),
    item_3: Item('spear', 30, (12, 19), 'weapon', 5),
    item_4: Item('sword', 25, (3, 5), 'weapon', 4),
    item_5: Item('pot', 10, (40, 8), 'tool', 10)
    }

#print(game_items[item_1].location[0])

objs.extend((item_1, item_2, item_3, item_4, item_5))


pygame.init()
#Initialize pygame dependent variables
flags = DOUBLEBUF
DISPLAYSURF = pygame.display.set_mode((WIDTH*TILESIZE, HEIGHT*TILESIZE), flags)
DISPLAYSURF.set_alpha(None)
player = pygame.image.load('assets/player-idea.png')
#pygame.display.set_mode((WIDTH * TILESIZE, HEIGHT * TILESIZE))
playerPos = [WIDTH / 2, HEIGHT / 2]
clock = pygame.time.Clock()
first_it = True
game_running = True

    
while True:
    pygame.time.set_timer(USEREVENT, 900)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit
        elif (event.type == USEREVENT):
            print("GAME END")
            game_running = False
            
            
    if (game_running):
        pX = playerPos[0] #25
        pY = playerPos[1]
        oX = game_items[item_1].location[0] #10
        oY = game_items[item_1].location[1]
      
        #Generate random direction, move, calculate if closer, move again.
        newDistance = calculate_distance(pX, pY, oX, oY)
        if (pX == oX and pY == oY):
            #Collect item
            print("FOUND ITEM")
        if (first_it or newDistance > oldDistance):
            [d, v] = random_move()
            lastMove = (d, v)
            first_it = False
            playerPos[d] += v
        else:
            #repeat last move
            playerPos[d] += v
        
        oldDistance = calculate_distance(pX, pY, oX, oY)
    
        for row in range(HEIGHT):
            for column in range(WIDTH):
                DISPLAYSURF.blit(SAND, (column * TILESIZE, row * TILESIZE))
                DISPLAYSURF.blit(player, (playerPos[0] * TILESIZE,(playerPos[1]) * TILESIZE))
        
        for i in game_items:
            DISPLAYSURF.blit(item_1, (game_items[i].location[0] * TILESIZE, game_items[i].location[1] * TILESIZE))
            pass
    
        pygame.display.update()
        clock.tick(60)
