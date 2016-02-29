#Current ouput should be the list of items in descending order
from functions import *
from classes import *
import pygame
from pygame.locals import *
import sys
import math
import random

objs = [] 
time_input = int(raw_input("Enter a time: "))

ASCENDING = False
WIDTH = 50
HEIGHT = 30
TILESIZE = 32
BLUE = (0, 0, 255)
TIME = time_input * 1000
SAND = pygame.image.load('assets/sand.png')

#Initialize items
item_1 = pygame.image.load('assets/crown.png')
item_2 = pygame.image.load('assets/sword.png')
item_3 = pygame.image.load('assets/spearhead.png')
item_4 = pygame.image.load('assets/bone1.png')
item_5 = pygame.image.load('assets/key1.png')


game_items = {    
    item_1: Item('coin', 2, (10, 10), 'treasure', 10, False),
    item_2: Item('crown', 200, (14, 1), 'treasure', 2, False),
    item_3: Item('spear', 30, (12, 19), 'weapon', 5, False),
    item_4: Item('sword', 25, (3, 5), 'weapon', 4, False),
    item_5: Item('pot', 10, (40, 8), 'tool', 10, False)
    }

#Sort the items
items = [item_1, item_2, item_3, item_4, item_5]
for i in range(len(game_items)):
    objs.append(game_items[items[i]])

if ASCENDING == True:
    sorted_list = sort_objects(objs)
else:
    sorted_list = sort_objects(objs)[::-1]

pygame.init()
#Initialize pygame dependent variables
flags = DOUBLEBUF
DISPLAYSURF = pygame.display.set_mode((WIDTH*TILESIZE, HEIGHT*TILESIZE + 40), flags)
DISPLAYSURF.set_alpha(None)
clock = pygame.time.Clock()
player = pygame.image.load('assets/player-idea.png')
pygame.time.set_timer(USEREVENT, TIME)

#place player in the middle of the screen
playerPos = [WIDTH / 2, HEIGHT / 2]
first_it = True
game_running = True
searchingFor = 1
    
while True:   
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit
        elif (event.type == USEREVENT):
            print("GAME END")
            game_running = False
            #run scoreboard code

    if (game_running):
        pX = playerPos[0]
        pY = playerPos[1]
        #Code that gets coordinates for object being searched for
        for i in range(1, len(game_items) + 1):
            if searchingFor == i:
                oX = sorted_list[i - 1].location[0]
                oY = sorted_list[i - 1].location[1]
            elif (i > len(game_items)):
                game_running = False
      
        #Generate random direction, move, calculate if closer, move again.
        if (pX == oX and pY == oY):
            #Collect item
            for i in game_items:
                if (pX == game_items[i].location[0] and pY == game_items[i].location[1]):
                    game_items[i].hidden = True
            print("FOUND ITEM")
            searchingFor += 1
        if (pX < oX):
            playerPos[0] += 1
        elif (pX > oX):
            playerPos[0] -= 1
        if (pY < oY):
            playerPos[1] += 1
        elif (pY > oY):
            playerPos[1] -= 1
        
        for row in range(HEIGHT):
            for column in range(WIDTH):
                DISPLAYSURF.blit(SAND, (column * TILESIZE, row * TILESIZE))
                DISPLAYSURF.blit(player, (playerPos[0] * TILESIZE,(playerPos[1]) * TILESIZE))
        
        for i in game_items:
            if (game_items[i].hidden != True):
                DISPLAYSURF.blit(i, (game_items[i].location[0] * TILESIZE, game_items[i].location[1] * TILESIZE))
    
        pygame.display.update()
        clock.tick(60)
