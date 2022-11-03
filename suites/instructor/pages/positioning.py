from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        OpenDU.clearScreen()

        pageBegin = Suite.renderMenu()

        options = [
            [Suite.activeAirport,"Suite.keyboard('Airport ICAO', 'Suite.navdataSearchAirport()')"], 
            ["RWY "+Suite.activeRunway,"Suite.comboBox('Runway Selection', 'Suite.navdataRunways()')"],
            ["Exit","action"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 350, 0, pageBegin[0], 'left', 'top', 110, 110, options)

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(100,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(400,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(700,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/runway.png')
        OpenDU.screen.blit(surface,(1000,quickActions[1] - 120))

        Suite.renderBottomMenu()
        Suite.dialogs()