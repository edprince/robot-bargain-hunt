import pygame
import time
import random

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)
event=pygame.event.get()


def screenmessage(text,color, font): #printing message on screen for the pause menu
    screentext = font.render(text, True, color, font)
    gameDisplay.blit(screentext, (20,250,20,400))


def pause():
    paused=True #pause variable

    while paused: #main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    pause()
                    
#gameDisplay.fill(white)
screenmessage("Game Paused, press C to continue or Q to quit", black, font)
pygame.display.update()
clock.tick(300)
pause()
pygame.quit()
quit()



    
            
