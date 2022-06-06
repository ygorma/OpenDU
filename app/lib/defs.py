# Funcoes
import pygame

class OpenDU:

    def text(text, font, color, xposition, yposition):

        myfont = pygame.font.SysFont(font, 30)
        textsurface = myfont.render(text, True, color)
        OpenDU.screen.blit(textsurface,(xposition,yposition))