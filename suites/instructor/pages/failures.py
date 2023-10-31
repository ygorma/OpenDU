from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        pageBegin = Suite.renderMenu()

        OpenDU.text("Situation Setup", Suite.font, (255,255,255), 20, pageBegin[0] + 25, Suite.fontSize)

        options = [
            ["Change Section","Suite.comboBox('ATA Sections', 'Suite.ataSections()')"], 
            ["Clear Failures","OpenDU.doNothing()"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 500, 0, pageBegin[0] + 50, 'left', 'top', 200, 50, options)

        OpenDU.text("ATA "+ str(Suite.activeAta) +" Available Failures", Suite.font, (255,255,255), 20, quickActions[1], Suite.fontSize)

        Suite.renderBottomMenu()
        Suite.dialogs()