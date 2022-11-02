from app.lib.defs import *

class Suite:

    dialogIsOpen = 0
    alertIsOpen = 0
    alertText = None
    alertFunction = None
    alertColor = None
    comboBoxIsOpen = 0
    comboBoxText = None
    comboBoxFunction = None

    refAirport = ""
    activeRunway = ""
    runwaysCache = ""

    def init(page):

        pagesPath = 'suites.instructor.pages'
        defaultPage = getattr(__import__(pagesPath, fromlist=[page]), page)
        defaultPage.Instructor.init()
    
    def button(text, font, fontSize, color, xposition, yposition, xsize, ysize, border, function, active=0):

        # Fake Text
        myfont = pygame.font.SysFont(font, fontSize)
        textsurface = myfont.render(text, True, color)

        # Adjustments
        textXposition = xposition + xsize/2 - textsurface.get_rect().width/2
        textYposition = yposition + (ysize/2) - (textsurface.get_rect().height/2)

        # Colors
        COLOR_BUTTON = (82,74,66)
        COLOR_BUTTON_BORDER = (115,107,107)
        COLOR_BUTTON_HOVER = (25,189,173)
        COLOR_BUTTON_ACTIVE = (74,230,66)

        # Rectangular
        rect = pygame.Rect(xposition, yposition, xsize, ysize)
        button = pygame.draw.rect(OpenDU.screen, COLOR_BUTTON, rect)
        rectBorder = pygame.Rect(xposition, yposition, xsize, ysize)
        pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_BORDER, rectBorder, border)

        # Text
        OpenDU.text(text, font, color, textXposition, textYposition)

        # Is Active
        if active:
            rectActive = pygame.Rect(xposition+border, yposition+border, xsize-border*2, ysize-border*2)
            pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_ACTIVE, rectActive, border)

        # If Dialog is open, cancel mouse
        if Suite.dialogIsOpen:
            pass
        else:
            if button.collidepoint(pygame.mouse.get_pos()):
                rectActive = pygame.Rect(xposition+border, yposition+border, xsize-border*2, ysize-border*2)
                pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_HOVER, rectActive, border)
                if OpenDU.leftClick:
                    OpenDU.log('INFO', 'Clicked on button: ' + text)
                    eval(function)

    def buttonDialog(text, font, fontSize, color, xposition, yposition, xsize, ysize, border, function):

        # Fake Text
        myfont = pygame.font.SysFont(font, fontSize)
        textsurface = myfont.render(text, True, color)

        # Adjustments
        textXposition = xposition + xsize/2 - textsurface.get_rect().width/2
        textYposition = yposition + (ysize/2) - (textsurface.get_rect().height/2)

        # Colors
        COLOR_BUTTON = (82,74,66)
        COLOR_BUTTON_BORDER = (115,107,107)
        COLOR_BUTTON_HOVER = (25,189,173)

        # Rectangular
        rect = pygame.Rect(xposition, yposition, xsize, ysize)
        button = pygame.draw.rect(OpenDU.screen, COLOR_BUTTON, rect)
        rectBorder = pygame.Rect(xposition, yposition, xsize, ysize)
        pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_BORDER, rectBorder, border)

        # Text
        OpenDU.text(text, font, color, textXposition, textYposition)

        # Is Hover
        if button.collidepoint(pygame.mouse.get_pos()):
            rectActive = pygame.Rect(xposition+border, yposition+border, xsize-border*2, ysize-border*2)
            pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_HOVER, rectActive, border)
            if OpenDU.leftClick:
                OpenDU.log('INFO', 'Clicked on dialog button: ' + text)
                eval(function)

        
    def div(xposition, yposition, xsize, ysize, color):

        # Rectangular
        rect = pygame.Rect(xposition, yposition, xsize, ysize)
        pygame.draw.rect(OpenDU.screen, color, rect)

    def menu(menuColor, menuMargin, menuXsize, menuXposition, menuYposition, xReference, yReference, itemsXsize, itemsYsize, items, isDialog=0):

        # Required Lines Calculation
        itemsNum = len(items)
        itemsPerline = math.floor((menuXsize-menuMargin)/(itemsXsize+menuMargin))
        lines = math.ceil(itemsNum/itemsPerline)
        menuHeight = ((itemsYsize+menuMargin)*lines)+menuMargin

        # Reference Adjustment
        if xReference == 'left':
            pass
        else:
            menuXposition = OpenDU.screen.get_width() - menuXsize - menuXposition
            
        if yReference == 'top':
            pass
        else:
            menuYposition = OpenDU.screen.get_height() - menuHeight - menuYposition

        # Rectangular
        Suite.div(menuXposition, menuYposition, menuXsize, menuHeight, menuColor)

        # First Item
        Actualx = menuXposition + menuMargin
        Actualy = menuYposition + menuMargin

        for id, item in enumerate(items, 0): 

            if isDialog:

                try:
                    items[id][2]
                except:
                    Suite.buttonDialog(items[id][0], 'suites/instructor/Geneva.ttf', 30, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1])
                        
                else:        
                    Suite.buttonDialog(items[id][0], 'suites/instructor/Geneva.ttf', 30, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1], OpenDU.activePage(items[id][2]))

            else:

                try:
                    items[id][2]
                except:
                    Suite.button(items[id][0], 'suites/instructor/Geneva.ttf', 30, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1])
                        
                else:        
                    Suite.button(items[id][0], 'suites/instructor/Geneva.ttf', 30, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1], OpenDU.activePage(items[id][2]))
            
            # Next Item
            Actualx += itemsXsize + menuMargin

            if ((id+1) % itemsPerline) == 0:
                Actualy += itemsYsize + menuMargin
                Actualx = menuXposition + menuMargin

        return (menuHeight, (menuYposition + menuHeight + menuMargin))

    def renderMenu():

        options = [
            ["Main","OpenDU.switchPage('main')","main"], 
            ["Positioning","OpenDU.switchPage('positioning')","positioning"],
            ["Weight & Balance","OpenDU.switchPage(page)","weightbalance"],
            ["Weather","OpenDU.switchPage(page)","weather"],
            ["Failures","OpenDU.switchPage(page)","failures"],
            ["Map","OpenDU.switchPage(page)","map"],
            ["Freeze","OpenDU.freezeSim()"],
            ["Exit","OpenDU.kill()"]
        ]

        menuWidth = OpenDU.screen.get_width() * 0.9

        menuLimits = Suite.menu((82,74,66), 10, menuWidth, 0, 0, 'left', 'top', 230, 40, options)

        Suite.clock(menuLimits)
        
        return menuLimits

    def renderBottomMenu():

        options = [
            ["< Prev Page","OpenDU.switchPage('main')"], 
            ["Next Page >","OpenDU.switchPage('positioning')"],
            ["- Brightness","OpenDU.decBrightness()"],
            ["Brightness +","OpenDU.incBrightness()"],
            ["Confirm Changes","OpenDU.switchPage('positioning')"]
        ]
        
        return Suite.menu((82,74,66), 10, OpenDU.screen.get_width(), 0, 0, 'left', 'bottom', 250, 40, options)

    def alert(text, function, color):

        Suite.dialogIsOpen = 1
        Suite.alertIsOpen = 1
        Suite.alertText = text
        Suite.alertFunction = function
        Suite.alertColor = color

    def alertClose(function):

        eval(function)

        Suite.dialogIsOpen = 0
        Suite.alertIsOpen = 0
        Suite.alertText = None
        Suite.alertFunction = None
        Suite.alertColor = None

    def comboBox(title, function): 

        # funtion must return a list

        Suite.dialogIsOpen = 1
        Suite.comboBoxIsOpen = 1
        Suite.comboBoxText = title
        Suite.comboBoxFunction = function

    def comboBoxClose(var, string): 

        setattr(Suite, var, ""+string+"")

        Suite.dialogIsOpen = 0
        Suite.comboBoxIsOpen = 0
        Suite.comboBoxText = None
        Suite.comboBoxFunction = None

    def dialogs():

        if Suite.dialogIsOpen:

            # Focus Alpha
            rect = pygame.Surface((OpenDU.screen.get_width(),OpenDU.screen.get_height()), pygame.SRCALPHA, 32)
            rect.fill((0, 0, 0, 200))
            OpenDU.screen.blit(rect, (0,0))

            if Suite.alertIsOpen:

                fontSize = 30
                sizex = 640
                sizey = 280
                positionx = (OpenDU.screen.get_width() - sizex)/2
                positiony = (OpenDU.screen.get_height() - sizey)/2

                COLOR_TEXT = (255,255,255)
                COLOR_BUTTON_BORDER = (115,107,107)

                # Fake Text
                myfont = pygame.font.SysFont('suites/instructor/Geneva.ttf', fontSize)
                textsurface = myfont.render(Suite.alertText, True, COLOR_TEXT)

                # Adjustments
                textXposition = positionx + sizex/2 - textsurface.get_rect().width/2
                textYposition = positiony + (sizey/2) - (textsurface.get_rect().height/2)

                # Main Rect With Border
                Suite.div(positionx, positiony, sizex, sizey, Suite.alertColor)

                rectBorder = pygame.Rect(positionx, positiony, sizex, sizey)
                pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_BORDER, rectBorder, 10)

                # Text Placing
                OpenDU.text(Suite.alertText, 'suites/instructor/Geneva.ttf', COLOR_TEXT, textXposition, textYposition - 35, fontSize)

                # Button
                Suite.buttonDialog("OK", 'suites/instructor/Geneva.ttf', 30, COLOR_TEXT, (positionx+(sizex/2))-125, (positiony+sizey)-100, 250, 40, 3, 'Suite.alertClose(\''+Suite.alertFunction+'\')' )

            if Suite.comboBoxIsOpen:

                fontSize = 30
                sizex = 300
                sizey = 60
                positionx = (OpenDU.screen.get_width() - sizex)/2
                positiony = 150

                COLOR_TEXT = (255,255,255)
                COLOR_BUTTON_BORDER = (115,107,107)

                # Fake Text
                myfont = pygame.font.SysFont('suites/instructor/Geneva.ttf', fontSize)
                textsurface = myfont.render(Suite.comboBoxText, True, COLOR_TEXT)

                # Adjustments
                textXposition = positionx + sizex/2 - textsurface.get_rect().width/2

                # Text Placing
                OpenDU.text(Suite.comboBoxText, 'suites/instructor/Geneva.ttf', COLOR_TEXT, textXposition, positiony - 50, fontSize)

                options = eval(Suite.comboBoxFunction)

                Suite.menu((82,74,66), 0, sizex, positionx, positiony, 'left', 'top', sizex, sizey, options, True)
    
    def clock(menuLimits):

        positionx = OpenDU.screen.get_width() * 0.9
        positiony = 0
        sizex = OpenDU.screen.get_width() * 0.1
        sizey = menuLimits[0]
        clockTime = time.strftime('%H:%M:%S %p')
        COLOR_BORDER = (115,107,107)

        # Fake Text
        myfont = pygame.font.SysFont('suites/instructor/Geneva.ttf', 30)
        textsurface = myfont.render(clockTime, True, (255,255,255))

        # Adjustments
        textXposition = positionx + sizex/2 - textsurface.get_rect().width/2
        textYposition = positiony + (sizey/2) - (textsurface.get_rect().height/2)

        # Main Rect With Border
        Suite.div(positionx, positiony, sizex, sizey, (82,74,66))

        rectBorder = pygame.Rect(positionx+10, positiony+10, sizex-20, sizey-20)
        pygame.draw.rect(OpenDU.screen, COLOR_BORDER, rectBorder, 3)

        # Text Placing
        OpenDU.text(clockTime, 'suites/instructor/Geneva.ttf', (255,255,255), textXposition, textYposition, 30)

    def navdataRunways():

        Airports = re.search("(A,KLAX)(.+?)(\n\n)", OpenDU.navdataAirports, re.DOTALL)
        Airports = Airports.group(0).split("\n")
        runwaysCache = []

        for runway in Airports:
            if runway.startswith('R,'):

                runwayData = runway.split(",")

                runwaysCache.append(["RWY "+runwayData[1]+"", "Suite.comboBoxClose('activeRunway', '"+runwayData[1]+"')"])

        return runwaysCache

    def navdataAirport():

        string = '(A,'+OpenDU.config.get('lastflight','airport')+')(.+?)(\n)';

        textfile = open('navdata\Airports.txt', 'r')
        filetext = textfile.read()
        textfile.close()
        matches = re.match(string, filetext)

        