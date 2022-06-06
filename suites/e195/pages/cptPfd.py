import os, sys
import pygame
from app.lib.defs import *

class eJets:

    def init():

        width, height = pygame.display.get_surface().get_size()

        # Posicionar Fundo
        logoImg = pygame.image.load(OpenDU.textures  + 'PFD_BG.png')
        logoImg = pygame.transform.scale(logoImg, (width, height))
        OpenDU.screen.blit(logoImg, (0,0)) 

        OpenDU.text('Teste', OpenDU.config.get('main','font'), (255,255,255), 0, 0)