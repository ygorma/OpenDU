from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        OpenDU.clearScreen()

        pageBegin = Suite.renderMenu()

        options = [
            ["ICAO","action"], 
            ["RWY","OpenDU.actualPage = page"],
            ["Weather","action"],
            ["Failures","action"],
            ["Freeze","action"],
            ["Map","action"],
            ["Exit","action"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 450, 0, pageBegin[0], 110, 110, options)

        print(quickActions)


        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(100,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(400,quickActions[1] + 100))

        surface = pygame.image.load(OpenDU.suitePath+'/texture/plane_90.png')
        OpenDU.screen.blit(surface,(700,quickActions[1] + 100))