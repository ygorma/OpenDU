from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        pageBegin = Suite.renderMenu()

        # Airport Selection

        OpenDU.text("Airport Selection", Suite.font, (255,255,255), 20, pageBegin[0] + 25, Suite.fontSize)

        options = [
            [Suite.activeAirport,"Suite.keyboard('Airport ICAO', 'Suite.navdataSearchAirport()', 'Search')"], 
            ["RWY "+Suite.activeRunway,"Suite.comboBox('Runway Selection', 'Suite.navdataRunways()')"],
            ["GATE "+Suite.activeGate,"Suite.comboBox('Gate Selection', 'Suite.navdataGates()')"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 450, 0, pageBegin[0] + 50, 'left', 'top', 110, 110, options)

        # Pushback Options

        OpenDU.text("Pushback Options", Suite.font, (255,255,255), 450, pageBegin[0] + 25, Suite.fontSize)

        options = [
            ["Left","action"], 
            ["Center","action"],
            ["Right","action"]
        ]

        pushbackActions = Suite.menu((0,0,0), 20, 450, 430, pageBegin[0] + 50, 'left', 'top', 110, 110, options)

        # Repositioning

        height = 350
        top_margin = quickActions[1]
        line_3_top_margin = top_margin + height - (height/3)

        Suite.button("3nm", Suite.font, Suite.fontSize, (255, 255, 255), 20, line_3_top_margin, 110, 110, 3, OpenDU.doNothing, active=0)

        image = pygame.image.load(OpenDU.textures + 'runway.png')
        scale = image.get_width()/image.get_height()
        image = pygame.transform.scale(image, (scale * (height/1.5),height/1.5))
        OpenDU.screen.blit(image, (100, top_margin))



        Suite.renderBottomMenu()
        Suite.dialogs()