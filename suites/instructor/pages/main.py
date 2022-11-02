from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        OpenDU.clearScreen()

        pageBegin = Suite.renderMenu()

        options = [
            ["TOGGLE DOORS","action"], 
            ["GRND PWR","OpenDU.actualPage = page"],
            ["GRND A/C","OpenDU.actualPage = page"],
            ["GRND AIR","Suite.alert('You have been alerted in RED!','OpenDU.doNothing()',(128,0,0))"],
            ["CHOCKS","Suite.alert('You have been alerted!','OpenDU.doNothing()',(82,74,66))"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 410, 0, pageBegin[0], 'left', 'top', 110, 110, options)

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(100,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(400,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(700,quickActions[1] + 100))

        Suite.renderBottomMenu()
        Suite.dialogs()