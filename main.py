#Code here independent of Pygame currently, keeping compatibility options open
#Current ouput should be the list of items in descending order
#from __future__ import division

from functions import *
from classes import *
import pygame
from pygame.locals import *
import sys
import math
import random
objs = []

def calculate_distance(x1, y1, x2, y2):
    width = math.sqrt((x2 - x1)**2)
    height = math.sqrt((y2 - y1)**2)
    return math.sqrt(height**2 + width**2)



WIDTH = 50
HEIGHT = 30
TILESIZE = 32
BLUE = (0, 0, 255)
#Initialize items

item_1 = 1
item_2 = 2
item_3 = 3
item_4 = 4
item_5 = 5


game_items = {    
    item_1: Item('coin', 2, (10, 10), 'treasure', 10),
    item_2: Item('crown', 200, (14, 1), 'treasure', 2),
    item_3: Item('spear', 30, (12, 19), 'weapon', 5),
    item_4: Item('sword', 25, (3, 5), 'weapon', 4),
    item_5: Item('pot', 10, (40, 8), 'tool', 10)
    }

print(game_items[item_1].location[0])

objs.extend((item_1, item_2, item_3, item_4, item_5))
#sorted_list = sort_objects(objs)
#for i in range(len(sorted_list)):
#    print(sorted_list[i].name)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH*TILESIZE, HEIGHT*TILESIZE))
player = pygame.image.load('assets/player-idea.png')
pygame.display.set_mode((WIDTH * TILESIZE, HEIGHT * TILESIZE))
playerPos = [WIDTH / 2, HEIGHT / 2]
#clock = pygame.time.Clock()
first_it = True

    
while True:
    #print(calculate_distance(pX, pY, oX, oY))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit

    
           
    pX = playerPos[0] #25
    pY = playerPos[1]
    oX = game_items[item_1].location[0] #10
    oY = game_items[item_1].location[1]
      
    newDistance = calculate_distance(pX, pY, oX, oY)
    if not first_it:
        print(newDistance, oldDistance)
    if (first_it or newDistance > oldDistance):
        [d, v] = random_move()
        lastMove = (d, v)
        first_it = False
        playerPos[d] += v
        print('new move')
    else:
        #repeat last move
        playerPos[d] += v
        
    oldDistance = calculate_distance(pX, pY, oX, oY)
    
            
    #Generate random direction, move, calculate if closer, move again.
        
    
    for row in range(HEIGHT):
        for column in range(WIDTH):
            DISPLAYSURF.fill((0, 0, 0))
            DISPLAYSURF.blit(player, (playerPos[0] * TILESIZE,(playerPos[1]) * TILESIZE))
            pass
        
    for i in game_items:
        #print(game_items[i].location)
        pygame.draw.circle(DISPLAYSURF, BLUE, (game_items[i].location[0] * 32, game_items[i].location[1] * 32), 20, 0)

    pygame.display.update()
    #clock.tick(60)
