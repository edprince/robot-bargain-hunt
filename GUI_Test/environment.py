import pygame
import graphics
import GuiBase
from constants import *



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
        self.surface.fill((DARKGRAY))
        self.gui_group = pygame.sprite.Group()
        self.square = GuiBase.VisualElement(40,40,40,40,(LIGHTGRAY))
        self._square = GuiBase.ClickableElement(70,70,70,70,(150,150,150))
        self.low_square = GuiBase.ClickableElement(300,300,40,40,(LIGHTGRAY))

        self.gui_group.add(self.square, self._square, self.low_square)



    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Hello")
            if event.type == pygame.QUIT:
                self.termianate()

    def update(self):
        pass

    def render(self):
        self.gui_group.draw(self.surface)
        self._square.render_text('Hello')
        self._square.render_text('World',((20,20)))
        self._square.render_text('!',((40,40)))
        self.

        self.low_square.render_text('This is a really long string')

        pygame.display.flip()
