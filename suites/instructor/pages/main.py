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

        Suite.renderBottomMenu()
        Suite.dialogs()