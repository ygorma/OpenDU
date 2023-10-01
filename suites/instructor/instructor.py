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
    keyboardIsOpen = 0
    keyboardText = None
    keyboardFunction = None
    font = OpenDU.suitePath + "fonts\\Geneva.ttf"
    fontSize = 20

    activeAirport = OpenDU.config.get('lastflight','airport')
    activeRunway = OpenDU.config.get('lastflight','runway')
    runwaysCache = ""
    scratchpadText = ""

    def init(page):

        pagesPath = 'suites.instructor.pages'
        defaultPage = getattr(__import__(pagesPath, fromlist=[page]), page)
        defaultPage.Instructor.init()
    
    def button(text, font, fontSize, color, xposition, yposition, xsize, ysize, border, function, active=0):

        # Fake Text
        myfont = pygame.font.Font(font, fontSize)
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
        OpenDU.text(text, font, color, textXposition, textYposition, fontSize)

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
        myfont = pygame.font.Font(font, fontSize)
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
        OpenDU.text(text, font, color, textXposition, textYposition, fontSize)

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
                    Suite.buttonDialog(items[id][0], Suite.font, Suite.fontSize, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1])
                        
                else:        
                    Suite.buttonDialog(items[id][0], Suite.font, Suite.fontSize, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1], OpenDU.activePage(items[id][2]))

            else:

                try:
                    items[id][2]
                except:
                    Suite.button(items[id][0], Suite.font, Suite.fontSize, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1])
                        
                else:        
                    Suite.button(items[id][0], Suite.font, Suite.fontSize, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3, items[id][1], OpenDU.activePage(items[id][2]))
            
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

        print(2)

        Suite.dialogIsOpen = 1
        Suite.alertIsOpen = 1
        Suite.alertText = text
        Suite.alertFunction = function
        Suite.alertColor = color

    def alertClose(function):

        Suite.dialogIsOpen = 0
        Suite.alertIsOpen = 0
        Suite.alertText = None
        Suite.alertFunction = None
        Suite.alertColor = None

        eval(function)

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

    def keyboard(title, function): 

        # funtion must return a list

        Suite.dialogIsOpen = 1
        Suite.keyboardIsOpen = 1
        Suite.keyboardText = title
        Suite.keyboardFunction = function

    def keyboardClose(): 

        print(1)

        Suite.dialogIsOpen = 0
        Suite.keyboardIsOpen = 0
        Suite.keyboardText = None
        Suite.keyboardFunction = None

    def dialogs():

        if Suite.dialogIsOpen:

            # Focus Alpha
            rect = pygame.Surface((OpenDU.screen.get_width(),OpenDU.screen.get_height()), pygame.SRCALPHA, 32)
            rect.fill((0, 0, 0, 200))
            OpenDU.screen.blit(rect, (0,0))

            if Suite.alertIsOpen:

                sizex = 640
                sizey = 280
                positionx = (OpenDU.screen.get_width() - sizex)/2
                positiony = (OpenDU.screen.get_height() - sizey)/2

                COLOR_TEXT = (255,255,255)
                COLOR_BUTTON_BORDER = (115,107,107)

                # Fake Text
                myfont = pygame.font.Font(Suite.font, Suite.fontSize)
                textsurface = myfont.render(Suite.alertText, True, COLOR_TEXT)

                # Adjustments
                textXposition = positionx + sizex/2 - textsurface.get_rect().width/2
                textYposition = positiony + (sizey/2) - (textsurface.get_rect().height/2)

                # Main Rect With Border
                Suite.div(positionx, positiony, sizex, sizey, Suite.alertColor)

                rectBorder = pygame.Rect(positionx, positiony, sizex, sizey)
                pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_BORDER, rectBorder, 10)

                # Text Placing
                OpenDU.text(Suite.alertText, Suite.font, COLOR_TEXT, textXposition, textYposition - 35, Suite.fontSize)

                # Button
                Suite.buttonDialog("OK", Suite.font, Suite.fontSize, COLOR_TEXT, (positionx+(sizex/2))-125, (positiony+sizey)-100, 250, 40, 3, 'Suite.alertClose(\''+Suite.alertFunction+'\')' )

            if Suite.comboBoxIsOpen:

                sizex = 300
                sizey = 60
                positionx = (OpenDU.screen.get_width() - sizex)/2
                positiony = 150

                COLOR_TEXT = (255,255,255)
                COLOR_BUTTON_BORDER = (115,107,107)

                # Fake Text
                myfont = pygame.font.Font(Suite.font, Suite.fontSize)
                textsurface = myfont.render(Suite.comboBoxText, True, COLOR_TEXT)

                # Adjustments
                textXposition = positionx + sizex/2 - textsurface.get_rect().width/2

                # Text Placing
                OpenDU.text(Suite.comboBoxText, Suite.font, COLOR_TEXT, textXposition, positiony - 50, Suite.fontSize)

                options = eval(Suite.comboBoxFunction)

                Suite.menu((82,74,66), 0, sizex, positionx, positiony, 'left', 'top', sizex, sizey, options, True)

            if Suite.keyboardIsOpen:

                sizex = 60
                sizey = 60
                columns = 13
                menuMargin = 10
                menuSizeX = (sizex*columns)+(menuMargin*columns)+menuMargin
                positionx = (OpenDU.screen.get_width() - menuSizeX)/2
                positiony = 100

                COLOR_TEXT = (255,255,255)
                COLOR_BUTTON_BORDER = (115,107,107)

                # Fake Text
                myfont = pygame.font.Font(Suite.font, Suite.fontSize)
                textsurface = myfont.render(Suite.keyboardText, True, COLOR_TEXT)

                # Adjustments
                textXposition = positionx + menuSizeX/2 - textsurface.get_rect().width/2

                # Menu Title
                OpenDU.text(Suite.keyboardText, Suite.font, COLOR_TEXT, textXposition, positiony, Suite.fontSize)

                # Scratchpad
                positiony = positiony + 50
                myfont = pygame.font.Font(Suite.font, Suite.fontSize)
                textsurface = myfont.render(Suite.scratchpadText, True, COLOR_TEXT)

                ysize = 60
                border = 5

                # Adjustments
                textXposition = positionx + menuSizeX/2 - textsurface.get_rect().width/2
                textYposition = positiony + (ysize/2) - (textsurface.get_rect().height/2)

                # Colors
                COLOR_BUTTON_BORDER = (115,107,107)

                # Rectangular
                rect = pygame.Rect(positionx, positiony, menuSizeX, ysize)
                rectBorder = pygame.Rect(positionx, positiony, menuSizeX, ysize)
                pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_BORDER, rectBorder, border)

                # Text
                OpenDU.text(Suite.scratchpadText, Suite.font, COLOR_TEXT, textXposition, textYposition, Suite.fontSize)

                # Keys
                options = [
                    ["0", "Suite.scratchpad('0')"], 
                    ["1", "Suite.scratchpad('1')"], 
                    ["2", "Suite.scratchpad('2')"], 
                    ["3", "Suite.scratchpad('3')"], 
                    ["4", "Suite.scratchpad('4')"], 
                    ["5", "Suite.scratchpad('5')"], 
                    ["6", "Suite.scratchpad('6')"], 
                    ["7", "Suite.scratchpad('7')"], 
                    ["8", "Suite.scratchpad('8')"], 
                    ["9", "Suite.scratchpad('9')"], 
                    ["+", "Suite.scratchpad('+')"], 
                    ["-", "Suite.scratchpad('-')"], 
                    ["<-", "Suite.scratchpad('ERASE')"], # Line one
                    ["Q", "Suite.scratchpad('Q')"], 
                    ["W", "Suite.scratchpad('W')"], 
                    ["E", "Suite.scratchpad('E')"], 
                    ["R", "Suite.scratchpad('R')"], 
                    ["T", "Suite.scratchpad('T')"], 
                    ["Y", "Suite.scratchpad('Y')"], 
                    ["U", "Suite.scratchpad('U')"], 
                    ["I", "Suite.scratchpad('I')"], 
                    ["O", "Suite.scratchpad('O')"], 
                    ["P", "Suite.scratchpad('P')"], 
                    ["[", "Suite.scratchpad('[')"], 
                    ["]", "Suite.scratchpad(']')"], 
                    ["*", "Suite.scratchpad('*')"],  # Line Two
                    ["A", "Suite.scratchpad('A')"], 
                    ["S", "Suite.scratchpad('S')"], 
                    ["D", "Suite.scratchpad('D')"], 
                    ["F", "Suite.scratchpad('F')"], 
                    ["G", "Suite.scratchpad('G')"], 
                    ["H", "Suite.scratchpad('H')"], 
                    ["J", "Suite.scratchpad('J')"], 
                    ["K", "Suite.scratchpad('K')"], 
                    ["L", "Suite.scratchpad('L')"], 
                    [";", "Suite.scratchpad(';')"], 
                    ["{", "Suite.scratchpad('{')"], 
                    ["}", "Suite.scratchpad('}')"], 
                    ["/", "Suite.scratchpad('/')"],  # Line Three
                    ["Z", "Suite.scratchpad('Z')"], 
                    ["X", "Suite.scratchpad('X')"], 
                    ["C", "Suite.scratchpad('C')"], 
                    ["V", "Suite.scratchpad('V')"], 
                    ["B", "Suite.scratchpad('B')"], 
                    ["N", "Suite.scratchpad('N')"], 
                    ["M", "Suite.scratchpad('M')"], 
                    [",", "Suite.scratchpad(',')"], 
                    [".", "Suite.scratchpad('.')"], 
                    [":", "Suite.scratchpad(':')"], 
                    ["\"", "Suite.scratchpad('\"')"], 
                    ["?", "Suite.scratchpad('?')"], 
                    ["=", "Suite.scratchpad('=')"],  # Line Four
                ]

                keyboard = Suite.menu((82,74,66), menuMargin, menuSizeX, positionx, positiony + 100, 'left', 'top', sizex, sizey, options, True)
                positiony = keyboard[1]

                # Options

                options = [
                    ["Clear", "Suite.scratchpad('CLEAR')"], 
                    ["Cancel", "Suite.keyboardClose()"], 
                    ["Search", ""+Suite.keyboardFunction+""], 
                ]

                Suite.menu((82,74,66), menuMargin, menuSizeX, positionx, positiony + 30, 'left', 'top', 293.3, sizey, options, True)

    def scratchpad(text):

        if text == "ERASE":
            Suite.scratchpadText = Suite.scratchpadText[:-1]
        elif text == "CLEAR":
            Suite.scratchpadText = ""
        else:
            Suite.scratchpadText += text
    
    def clock(menuLimits):

        positionx = OpenDU.screen.get_width() * 0.9
        positiony = 0
        sizex = OpenDU.screen.get_width() * 0.1
        sizey = menuLimits[0]
        clockTime = time.strftime('%H:%M:%S %p')
        COLOR_BORDER = (115,107,107)

        # Fake Text
        myfont = pygame.font.Font(Suite.font, Suite.fontSize)
        textsurface = myfont.render(clockTime, True, (255,255,255))

        # Adjustments
        textXposition = positionx + sizex/2 - textsurface.get_rect().width/2
        textYposition = positiony + (sizey/2) - (textsurface.get_rect().height/2)

        # Main Rect With Border
        Suite.div(positionx, positiony, sizex, sizey, (82,74,66))

        rectBorder = pygame.Rect(positionx+10, positiony+10, sizex-20, sizey-20)
        pygame.draw.rect(OpenDU.screen, COLOR_BORDER, rectBorder, 3)

        # Text Placing
        OpenDU.text(clockTime, Suite.font, (255,255,255), textXposition, textYposition, Suite.fontSize)

    def navdataRunways():

        Airports = re.search("(A,"+Suite.activeAirport+")(.+?)(\n\n)", OpenDU.navdataAirports, re.DOTALL)
        Airports = Airports.group(0).split("\n")
        runwaysCache = []

        for runway in Airports:
            if runway.startswith('R,'):

                runwayData = runway.split(",")

                runwaysCache.append(["RWY "+runwayData[1]+"", "Suite.comboBoxClose('activeRunway', '"+runwayData[1]+"')"])

        runwaysCache.append(["Cancel", "Suite.comboBoxClose('activeRunway', '"+Suite.activeRunway+"')"])

        return runwaysCache

    def navdataSearchAirport():

        if Suite.scratchpadText == '':
            Suite.keyboardClose()
            Suite.alert('Airport ICAO cannot be blank.','Suite.keyboard("Airport ICAO", "Suite.navdataSearchAirport()")',(82,74,66))

        else:

            Airport = re.search("(A,"+Suite.scratchpadText+")(.+?)(\n\n)", OpenDU.navdataAirports, re.DOTALL)

            if Airport:

                Airport = Airport.group(0).split("\n")

                # Autoselect existing runway

                for runway in Airport:
                    if runway.startswith('R,'):
                        runwayData = runway.split(",")
                        Suite.activeRunway = runwayData[1]

                Suite.keyboardClose()
                Suite.activeAirport = Suite.scratchpadText
                Suite.scratchpadText = ""
            
            else:
                Suite.keyboardClose()
                Suite.alert(Suite.scratchpadText+' was not found!','Suite.keyboard("Airport ICAO", "Suite.navdataSearchAirport()")',(82,74,66))

        