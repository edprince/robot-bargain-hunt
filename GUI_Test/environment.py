import pygame
import graphics
import GuiBase
from constants import *
import sys



#SCREENWIDTH = 500
#SCREENHEIGHT = 500
#SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

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
        #self.surface.fill((RED))
        self.gui_group = pygame.sprite.Group()
        bckImg = pygame.image.load('map1.png').convert_alpha()
        self.surface.blit(bckImg, (0,0))
        self.square = GuiBase.VisualElement(800,450,200,100, (230,230,230))
        self._square = GuiBase.ClickableElement(70,70,70,70, (150,150,150))


        self.gui_group.add(self.square, self._square)



    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Hello")
            if event.type == pygame.QUIT:
                self.terminate()

    def update(self):
        pass

    def render(self):
        self.gui_group.draw(self.surface)
        self._square.on_hover((self._square.highlight))
        self._square.render_text('Hello')
        self._square.render_text('World',((20,20)))
        self._square.render_text('!',((40,40)))


        pygame.display.flip()
