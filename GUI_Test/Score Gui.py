import pygame
import time
import random
 
pygame.init()
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
Bright_green = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)
 
block_color = (53,115,255)
 
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('THE GAME NAME')
clock = pygame.time.Clock()
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((400,50))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Score:", largeText)
        TextRect.center = ((150,250))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 150+100 > mouse[0] > 150 and 520+50 > mouse[1] > 520:
            pygame.draw.rect(gameDisplay, Bright_green,(150,520,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(150,520,100,50))
            
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Again!", smallText)
        textRect.center = ( (150+(100/2)), (520+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        if 650+100 > mouse[0] > 650 and 520+50 > mouse[1] > 520:
            pygame.draw.rect(gameDisplay, bright_red,(650,520,100,50))
        else:
            pygame.draw.rect(gameDisplay, red,(650,520,100,50))
            
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Quit!", smallText)
        textRect.center = ( (650+(100/2)), (520+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(15)
        
game_intro()
pygame.quit()
quit()
