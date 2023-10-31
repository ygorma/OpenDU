import os, sys
import time
import pygame

class Splash: 

    def run():

        # Run
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Setup
        SplashWidth           = 640                     # In Pixels
        SplashHeight          = 480                     # In Pixels
        SplashBackgroundColor = [2,24,244]              # In RGB
        SplashLogoPath        = 'app/media/splash.png'  # Related to main application folder

        # Screen Rendering
        screen = pygame.display.set_mode((SplashWidth,SplashHeight),pygame.NOFRAME)
        background = pygame.Surface(screen.get_size())
        background.fill(SplashBackgroundColor)
        screen.blit(background, (0,0))

        # Set Icon
        pygame.display.set_icon(pygame.image.load('app\media\icon.png').convert())

        # Logo Positioning
        logoImg = pygame.image.load(SplashLogoPath).convert()
        logoImgX = (SplashWidth/2) - logoImg.get_width()/2
        logoImgY = (SplashHeight/2) - logoImg.get_height()/2
        screen.blit(logoImg, (logoImgX ,logoImgY))

        # Update Screen
        pygame.display.update()
        time.sleep(5)
        pygame.display.quit()