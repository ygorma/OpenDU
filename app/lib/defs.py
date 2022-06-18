import os, sys
import time
import socket
import configparser
import pickle
import pygame
from pygame import gfxdraw
import math
from datetime import datetime
from app.lib.splash import *

class OpenDU:

    def init():

        # Delete Last Log
        try:
            os.remove(OpenDU.logPath)
        except:
            pass

        # PyGame Init
        OpenDU.log('INFO', 'Initializing App')
        pygame.init()
        pygame.font.init()
        clock = pygame.time.Clock()

        # Splash
        if OpenDU.config.getint('main','splash'):
            OpenDU.log('INFO', 'Running Splash')
            Splash.run()

        # Screen Position
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (OpenDU.config.getint('main','xposition'),OpenDU.config.getint('main','yposition'))
        os.environ['SDL_VIDEO_CENTERED'] = '0'

        # Screen Setup
        pygame.display.set_caption('OpenDU - ' + OpenDU.config.get('main','window_name'))

        if OpenDU.fullscreen == 1:
            OpenDU.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        else:
            if OpenDU.frame == 1:
                OpenDU.screen = pygame.display.set_mode((OpenDU.config.getint('main','xsize'),OpenDU.config.getint('main','ysize')),pygame.RESIZABLE)
            else:
                OpenDU.screen = pygame.display.set_mode((OpenDU.config.getint('main','xsize'),OpenDU.config.getint('main','ysize')),pygame.NOFRAME)                                                 

        OpenDU.xsize, OpenDU.ysize = OpenDU.screen.get_size()

        # Try Connection
        OpenDU.initialConnection()

        # Finish Init
        OpenDU.log('INFO', 'Initializing Suite')

    def kill():

        # Terminate TCP Connection
        try:
            OpenDU.conn.close()
        except:
            OpenDU.log('INFO', 'Connection not closed. Never opened.')
        else:
            OpenDU.log('INFO', 'Connection closed.')

        # Prepare Settings
        position = os.environ['SDL_VIDEO_WINDOW_POS']
        xcoordinate, ycoordinate = position.split(',')

        # Save Settings
        OpenDU.config.set('main', 'xposition', str(xcoordinate))
        OpenDU.config.set('main', 'yposition', str(ycoordinate))
        OpenDU.config.set('main', 'xsize', str(OpenDU.xsize))
        OpenDU.config.set('main', 'ysize', str(OpenDU.ysize))
        OpenDU.config.set('main', 'frame', str(OpenDU.frame))

        # Write Settings
        with open('opendu.ini', 'w') as configfile:
            OpenDU.config.write(configfile)

        OpenDU.log('INFO', 'Open DU finished.')

        # Fechar OpenDU
        pygame.quit()
        sys.exit()
    
    def log(logType, text):

        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")

        with open(OpenDU.logPath, 'a') as file_object:
            file_object.write("[ "+current_time+" ] "+ logType +" | "+ text +"\n")

    def initialConnection():

        # Create Connection
        dots = 3
        dot = '.'
        OpenDU.log('INFO', 'Trying to connect on '+OpenDU.config.get('conn','server')+':'+OpenDU.config.get('conn','port')+'')

        while True:

            # Clear Screen
            OpenDU.clearScreen()

            # Activate Key Presses
            OpenDU.keyPress()

            try:
                OpenDU.conn.connect((OpenDU.config.get('conn','server'), OpenDU.config.getint('conn','port'))) 
                
            except:
                # Number of Dots
                if dots == 3:
                    dots = 1
                else:
                    dots += 1

                # Print Error
                OpenDU.text('Trying to Connect on '+ OpenDU.config.get('conn','server') +':'+ OpenDU.config.get('conn','port') + dot*dots, OpenDU.config.get('main','font'), (255,255,255), 10, 10)
                pygame.display.update()
                time.sleep(1)

            else:
                OpenDU.text('Connection Acquired!', OpenDU.config.get('main','font'), (255,255,255), 10, 10)
                OpenDU.log('INFO', 'Connection Acquired!')
                pygame.display.update()
                break;

        time.sleep(2)

    def clearScreen():

        OpenDU.screen.fill((0,0,0))

    def text(text, font, color, xposition, yposition):

        size = 30

        lines = text.split("\n ")
        lineQty = len(lines)

        if (lineQty % 2) == 0:
            startPositionY = yposition-(lineQty * size)

            for line in lines:
                myfont = pygame.font.SysFont(font, size)
                textsurface = myfont.render(line, True, color)
                OpenDU.screen.blit(textsurface,(xposition,startPositionY))
                startPositionY += size

        else: 
            startPositionY = yposition-(lineQty * size)       
            for line in lines:
                myfont = pygame.font.SysFont(font, size)
                textsurface = myfont.render(line, True, color)
                OpenDU.screen.blit(textsurface,(xposition,yposition))
                startPositionY += size


    def keyPress():

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #ESQ
                    OpenDU.kill()
                if event.key == pygame.K_TAB:    #TAB
                    OpenDU.frameChange()
                if event.key == pygame.K_RETURN:
                    OpenDU.frameFullscreen()
            if event.type == pygame.QUIT:
                OpenDU.kill()
            if event.type == pygame.VIDEORESIZE:
                OpenDU.screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)

        pygame.event.pump()

    def frameChange():

        if OpenDU.frame == 0:
            OpenDU.screen = pygame.display.set_mode((OpenDU.screen.get_width(),OpenDU.screen.get_height()),pygame.RESIZABLE)
            OpenDU.frame = 1
        else:
            OpenDU.screen = pygame.display.set_mode((OpenDU.screen.get_width(),OpenDU.screen.get_height()),pygame.NOFRAME)
            OpenDU.frame = 0

    def frameFullscreen():

        if OpenDU.fullscreen == 0:
            pygame.display.set_mode((0, 0))
            pygame.display.toggle_fullscreen()
            OpenDU.fullscreen = 1
        else:
            pygame.display.toggle_fullscreen()
            pygame.display.set_mode((OpenDU.config.getint('main','xsize'),OpenDU.config.getint('main','ysize')))
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (OpenDU.config.getint('main','xposition'),OpenDU.config.getint('main','yposition'))
            OpenDU.fullscreen = 0