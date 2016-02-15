import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,500))

bg = pygame.image.load("map1.png")


pygame.mouse.set_visible(0)

ship = pygame.image.load("map1.png")
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

screen.blit(ship, (ship_left,ship_top))



pygame.display.set_caption('galaxy invaders')

while True:
    clock.tick(60)
screen.fill((r,0,0))
screen.blit(bg, (0,0))
x,y = pygame.mouse.get_pos()
screen.blit(ship, (x-ship.get_width()/2, ship_top))
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
        shoot_y = 500
        shoot_x = x
