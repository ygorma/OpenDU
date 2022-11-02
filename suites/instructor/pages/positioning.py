from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        OpenDU.clearScreen()

        pageBegin = Suite.renderMenu()

        options = [
            ["ICAO","Suite.alert('Teste!')"], 
            ["RWY "+Suite.activeRunway+"","Suite.comboBox('Runway Selection', 'Suite.navdataRunways()')"],
            ["Exit","action"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 350, 0, pageBegin[0], 'left', 'top', 110, 110, options)

        Suite.renderBottomMenu()
        Suite.dialogs()