from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        pageBegin = Suite.renderMenu()

        OpenDU.text("Weather Presets", Suite.font, (255,255,255), 20, pageBegin[0] + 25, Suite.fontSize)

        options = [
            ["CAVOK","action"], 
            ["VFR","action"],
            ["MVFR","action"],
            ["NON-PREC.","action"],
            ["CAT I","action"],
            ["CAT II","action"],
            ["CAT III A","action"],
            ["CAT III B","action"],
            ["CAT III C","action"],
            ["REAL WX","action"]
        ]

        quickActions = Suite.menu((0,0,0), 20, 720, 0, pageBegin[0] + 50, 'left', 'top', 120, 50, options)

        OpenDU.text("Date & Time", Suite.font, (255,255,255), 740, pageBegin[0] + 25, Suite.fontSize)

        options = [
            ["Dawn","action"], 
            ["Day","action"],
            ["Dusk","action"],
            ["Night","action"],
            ["Ref. HLO", ""],
            ["Local HLO", ""],
            ["Set Date","Suite.keyboard('Set Date', 'Suite.environmentSetDate()', 'Set')"],
            ["Set Time","Suite.keyboard('Set Time (HLO)', 'Suite.environmentSetTime()', 'Set')"]
        ]

        timeActions = Suite.menu((0,0,0), 20, 646, 720, pageBegin[0] + 50, 'left', 'top', 120, 50, options)

        OpenDU.text("Custom Weather", Suite.font, (255,255,255), 20, quickActions[1], Suite.fontSize)

        Suite.renderBottomMenu()
        Suite.dialogs()