from ast import And
import os, sys
import time
import socket
import configparser
import pickle
import pygame
from pygame import gfxdraw
import math
import csv
from datetime import datetime
from app.lib.splash import *
import re

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
        OpenDU.clock = pygame.time.Clock()

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

        # Set Icon
        pygame.display.set_icon(pygame.image.load('app\media\icon.png'))

        # Load Navdata
        Airports = open('navdata/Airports.txt', 'r')
        OpenDU.navdataAirports = Airports.read()
        Airports.close()

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
        OpenDU.config['main']['xposition'] = str(xcoordinate)
        OpenDU.config['main']['yposition'] = str(ycoordinate)
        OpenDU.config['main']['xsize'] = str(OpenDU.xsize)
        OpenDU.config['main']['ysize'] = str(OpenDU.ysize)
        OpenDU.config['main']['frame'] = str(OpenDU.frame)
        OpenDU.config['main']['brightness'] = str(OpenDU.brightness)

        # Write Settings
        with open('opendu.ini', 'w') as configfile:
            OpenDU.config.write(configfile)

        OpenDU.log('INFO', 'OpenDU finished.')

        # Fechar OpenDU
        pygame.quit()
        sys.exit()
    
    def log(logType, text):

        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")

        with open(OpenDU.logPath, 'a') as file_object:
            MESSAGE = "[ "+current_time+" ] "+ logType +" | "+ text
            file_object.write(MESSAGE + "\n")
            print(MESSAGE)

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

    def text(text, font, color, xposition, yposition, size=30):

        lines = text.split("\\")
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

        # Key Vars
        OpenDU.leftClick = 0

        # Key Used
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    OpenDU.leftClick = 1

        pygame.event.pump()

    def frameChange():

        if OpenDU.frame == 0:
            OpenDU.screen = pygame.display.set_mode((OpenDU.screen.get_width(),OpenDU.screen.get_height()),pygame.RESIZABLE)
            OpenDU.frame = 1
        else:
            OpenDU.screen = pygame.display.set_mode((OpenDU.screen.get_width(),OpenDU.screen.get_height()),pygame.NOFRAME)
            OpenDU.frame = 0
            OpenDU.log('INFO', 'Switched to Windowed (No Frame).')

    def frameFullscreen():

        if OpenDU.fullscreen == 0:
            pygame.display.set_mode((0, 0))
            pygame.display.toggle_fullscreen()
            OpenDU.fullscreen = 1
            OpenDU.log('INFO', 'Switched to Fullscreen.')

        else:
            pygame.display.toggle_fullscreen()
            pygame.display.set_mode((OpenDU.config.getint('main','xsize'),OpenDU.config.getint('main','ysize')))
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (OpenDU.config.getint('main','xposition'),OpenDU.config.getint('main','yposition'))
            OpenDU.fullscreen = 0
            OpenDU.log('INFO', 'Switched to Windowed.')

    def switchPage(page):

        if OpenDU.actualPage != page:
            OpenDU.actualPage = page
            OpenDU.log('INFO', 'Page Changed to: ' + page)


    def activePage(page):

        if OpenDU.actualPage == page:
            return 1
        else:
            return 0

    def doNothing():
        # Def Reserved to "Do nothing" for actions that require a def fulfilled
        pass

    def incBrightness():

        if OpenDU.brightness >= 20:
            OpenDU.brightness -= 10
            if OpenDU.brightness <= 20:
                OpenDU.brightness = 0

    def decBrightness():

        if OpenDU.brightness < 230:
            OpenDU.brightness += 10
            if OpenDU.brightness > 230:
                OpenDU.brightness = 255
    
    def fpsCounter():

        if OpenDU.config.getint('main','showfps') == 1:
            OpenDU.clock.tick()
            fps = str(int(OpenDU.clock.get_fps()))
            OpenDU.text(fps, OpenDU.config.get('main','font'), (74,230,66), 10, 10, 15)