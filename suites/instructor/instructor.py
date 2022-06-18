from app.lib.defs import *

class Suite:

    def init(page):

        pagesPath = 'suites.instructor.pages'
        defaultPage = getattr(__import__(pagesPath, fromlist=[page]), page)
        defaultPage.Instructor.init()
    
    def button(text, font, fontSize, color, xposition, yposition, xsize, ysize, border):

        # Fake Text
        myfont = pygame.font.SysFont(font, fontSize)
        textsurface = myfont.render(text, True, color)

        # Adjustments
        textXposition = xposition + xsize/2 - textsurface.get_rect().width/2
        textYposition = yposition + (ysize/2) - (textsurface.get_rect().height/2)

        # Colors
        COLOR_BUTTON = (82,74,66)
        COLOR_BUTTON_BORDER = (115,107,107)
        COLOR_BUTTON_ACTIVE = (25,189,173)

        # Rectangular
        rect = pygame.Rect(xposition, yposition, xsize, ysize)
        button = pygame.draw.rect(OpenDU.screen, COLOR_BUTTON, rect)
        rectBorder = pygame.Rect(xposition, yposition, xsize, ysize)
        pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_BORDER, rectBorder, border)

        # Text
        OpenDU.text(text, font, color, textXposition, textYposition)

        # Active Option
        if button.collidepoint(pygame.mouse.get_pos()):
            rectActive = pygame.Rect(xposition+border, yposition+border, xsize-border*2, ysize-border*2)
            pygame.draw.rect(OpenDU.screen, COLOR_BUTTON_ACTIVE, rectActive, border)
        
    def div(xsize, ysize, xposition, yposition, color):

        # Rectangular
        rect = pygame.Rect(xposition, yposition, xsize, ysize)
        button = pygame.draw.rect(OpenDU.screen, color, rect)

    def menu(menuColor, menuMargin, menuXsize, menuXposition, menuYposition, itemsXsize, itemsYsize, items):

        itemsNum = len(items)
        itemsPerline = math.floor((menuXsize-menuMargin)/(itemsXsize+menuMargin))
        lines = math.ceil(itemsNum/itemsPerline)
        menuHeight = ((itemsYsize+menuMargin)*lines)+menuMargin

        # Rectangular
        Suite.div(menuXsize, menuHeight, menuXposition, menuYposition, menuColor)

        # First Item
        Actualx = menuXposition + menuMargin
        Actualy = menuYposition + menuMargin

        for id, item in enumerate(items, 0):            

            Suite.button(items[id][0], 'suites/instructor/Geneva.ttf', 30, (255,255,255), Actualx, Actualy, itemsXsize, itemsYsize, 3)
            
            # Next Item
            Actualx += itemsXsize + menuMargin

            if ((id+1) % itemsPerline) == 0:
                Actualy += itemsYsize + menuMargin
                Actualx = menuXposition + menuMargin

        return (menuHeight, menuYposition + menuHeight + menuMargin)
            
    def switchPage(page):

        OpenDU.actualPage = page

    def renderMenu():

        options = [
            ["Main","action"], 
            ["Positioning","OpenDU.actualPage = page"],
            ["Weight & Balance","OpenDU.actualPage = page"],
            ["Weather","action"],
            ["Failures","action"],
            ["Freeze","action"],
            ["Map","action"],
            ["Exit","action"]
        ]
        
        return Suite.menu((82,74,66), 10, OpenDU.screen.get_width(), 0, 0, 250, 40, options)