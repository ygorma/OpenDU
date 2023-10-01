import os, sys
import pygame
from app.lib.defs import *

class eJets:

    font = OpenDU.suitePath + "fonts\\EmbraerDefault.ttf"
    fontSize = 20

    def init():

        width, height = pygame.display.get_surface().get_size()

        # Posicionar Fundo
        logoImg = pygame.image.load(OpenDU.textures  + 'PFD_BG.svg')
        logoImg = pygame.transform.scale(logoImg, (width, height))
        OpenDU.screen.blit(logoImg, (0,0)) 

        OpenDU.text('125', eJets.font, (64,242,0), 100, 100)
        OpenDU.text('3000', eJets.font, (64,242,0), 100, 200)