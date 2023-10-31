from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        pageBegin = Suite.renderMenu()

        OpenDU.text("Ground Services", Suite.font, (255,255,255), 20, pageBegin[0] + 25, Suite.fontSize)

        options = [
            ["TOGGLE<br>DOORS","OpenDU.doNothing()"], 
            ["GROUND<br>PWR","OpenDU.doNothing()"],
            ["GROUND<br>A/C","OpenDU.doNothing()"],
            ["GROUND<br>AIR","Suite.alert('You have been alerted in RED!','OpenDU.doNothing()',(128,0,0))"],
            ["WHEEL<br>CHOCKS","Suite.alert('You have been alerted!','OpenDU.doNothing()',(82,74,66))"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 410, 0, pageBegin[0] + 50, 'left', 'top', 110, 110, options)

        Suite.renderBottomMenu()
        Suite.dialogs()