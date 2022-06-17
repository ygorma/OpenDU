from app.lib.defs import *

class Suite:

    def init(page):

        pagesPath = 'suites.instructor.pages'

        defaultPage = getattr(__import__(pagesPath, fromlist=[page]), page)
        defaultPage.instructor.init()
    
    def button(text, font, color, xposition, yposition):

        myfont = pygame.font.SysFont(font, 30)
        textsurface = myfont.render(text, True, color)
        OpenDU.screen.blit(textsurface,(xposition,yposition))