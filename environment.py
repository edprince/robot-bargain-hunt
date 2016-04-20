import pygame
import main
import graphics
import GuiBase
from constants import *
import sys
from pygame.locals import *
import main
import functions

class SceneBase():

    def __init__(self):
        self.next = self

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def termianate(self):
        pygame.quit()

class Environment(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.surface = graphics.SCREEN
        self.gui_group = pygame.sprite.Group()
        bckImg = pygame.image.load('map1.png') # loading an image of the map
        pygame.font.init()   # font initialisation
        myfont = pygame.font.Font('font1.ttf', 65)  # choosing the font
        myfont1 = pygame.font.Font('font1.ttf', 40)
        myfont2 = pygame.font.Font('font1.ttf', 30)
        title = myfont.render("IT BELONGS IN THE MUSEUM !", 1, (0,0,0))
        startTheGame = myfont1.render("PRESS 'ENTER' TO START", 1, (0,200,0))
        closeTheMenu = myfont2.render("PRESS 'Q' TO QUIT", 1, (180,0,0))
        self.surface.blit(bckImg, (0,0))  #blitting the background
        self.surface.blit(title, (375,80)) #blitting the title
        self.surface.blit(startTheGame, ((500),700))
        self.surface.blit(closeTheMenu, ((649),800))

    def paused(self):
        print("pause")
        bckImgP = pygame.image.load('mappause.png')
        my1 = pygame.font.Font('font1.ttf', 40)
        pausedText = my1.render("PAUSED", 1, (0,200,0))
        self.surface.blit(bckImgP, (0,0))
        self.surface.blit(pausedText, ((500),700))
        global pause
        pause = False
        while pause:
            for event in pygame.event.get(): # Menu control
                if event.type == pygame.KEYDOWN: 
                    if(event.key == pygame.K_q):
                        pause = False
                        print("unPause")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        pygame.display.update()
        

    def process_input(self):
        for event in pygame.event.get(): # Menu control
            if event.type == pygame.KEYDOWN: 
                if (event.key == K_RETURN):
                    print("START GAME")
                    main.start()
                    #if (event.key == K_RETURN) == True:
                    # Code block to start game here
                if(event.key == pygame.K_p):
                    pause = True
                    print("Pause")
                    self.paused()
                
                elif (event.key == K_q): # Quit game
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                elif (event.key == K_o):
                    pause = False
                    print("unpause")
                    pygame.display.update()
                    self.paused()


                    
    def update(self):
        pass
  

    def render(self):
        self.gui_group.draw(self.surface)
        pygame.display.flip()


