import pygame
import graphics
import GuiBase
from constants import *
import sys


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
        pygame.font.init()
        myfont = pygame.font.Font('font1.ttf', 65)
        title = myfont.render("IT BELONGS IN THE MUSEUM !", 1, (0,0,0))
        bckImg = pygame.image.load('map1.png')
        self.surface.blit(bckImg, (0,0))
        self.surface.blit(title, (375,80))
        self._square = GuiBase.ClickableElement(70,70,70,70, (150,150,150))
        self.start = GuiBase.ClickableElement(477, 646, 180, 100, (0,204,0))
        self.exit = GuiBase.ClickableElement(954, 646, 180, 100, (204, 0, 0))


        self.gui_group.add(self.start,self.exit)



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
        self.start.on_hover((self.start.highlight))
        self.exit.on_hover((self.exit.highlight))
        self.start.render_text('Start')
        self.exit.render_text('Exit')



        pygame.display.flip()
