

from msilib.schema import Class
from suites.e195.pages.cptMCDU import *
from suites.e195.e195 import *

class page():

    def __init__(self):

        options = [
            ["RADIO",(255,255,255)],    # Page Title
            ["1/2",(255,255,255)],      # Page Number

            # Row 1
            [
                ["COM1",(255,255,255)],         
                ["⇆130.85",(64,242,0)],     
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["COM2",(255,255,255)],
                ["121.60⇆",(64,242,0)]
            ],

            # Row 2
            [
                ["25K",(255,255,255)],         
                ["◀130.85",(255,255,255)],     
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["25K",(255,255,255)],
                ["121.60 ",(255,255,255)],
            ],

            # Row 3
            [
                ["NAV1",(255,255,255)],         
                ["⇆130.85",(64,242,0)],     
                ["FMS   FMS",(64,242,0)],
                ["AUTO AUTO",(64,242,0)],
                ["NAV2",(255,255,255)],
                ["121.60⇆",(64,242,0)],
            ],

            # Row 4
            [
                ["",(255,255,255)],         
                [" 130.85",(255,255,255)],     
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["121.60 ",(255,255,255)],
            ],

            # Row 5
            [
                ["",(255,255,255)],         
                ["◀TCAS/XPDR",(255,255,255)],     
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["XPDR1",(255,255,255)],
                ["2000 ",(64,242,0)],
            ],

            # Row 6
            [
                ["",(255,255,255)],         
                ["●STBY TA/RA",(255,255,255)],     
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["",(255,255,255)],
                ["IDENT ",(255,255,255)],
            ]
        ]

        top_distances = primusEpic.buildMenu(options)

        pygame.draw.lines(OpenDU.screen, (255,255,255), False, 
                          [((OpenDU.xsize/2),130),
                           ((OpenDU.xsize/2),top_distances[1] + 3), 
                           ((OpenDU.xsize-110),top_distances[1] + 3), 
                           (110,top_distances[1] + 3), 
                           ((OpenDU.xsize/2),top_distances[1] + 3), 
                           ((OpenDU.xsize/2),top_distances[3] + 3), 
                           ((OpenDU.xsize-110),top_distances[3] + 3), 
                           (110,top_distances[3] + 3)]
        , width=2)