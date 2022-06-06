import os, sys
import time
import pygame

class Splash: 

    def init():

        # Inicializar
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        # Configuracao da Tela
        screen = pygame.display.set_mode((800,600),pygame.NOFRAME)
        background = pygame.Surface(screen.get_size())
        background.fill((2,24,244))
        screen.blit(background, (0,0))

        # Posicionar Logo
        logoImg = pygame.image.load('app/media/logo.png')
        logoImgX = (800/2) - logoImg.get_width()/2
        logoImgY = (600/2) - logoImg.get_height()/2
        screen.blit(logoImg, (logoImgX ,logoImgY))

        # Atualizar Tela
        pygame.display.update()
        time.sleep(5)
        pygame.quit()