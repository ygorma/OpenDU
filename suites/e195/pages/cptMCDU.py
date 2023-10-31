from app.lib.defs import *
from suites.e195.e195 import *

class primusEpic:

    fontSize = 10
    pageNum = ""
    currentPage = "radio"
    currentSubPage = 1

    def init():

        pagesPath = 'suites.e195.pages.MCDU'

        MCDU = pygame.image.load(OpenDU.textures + 'mcdu.png')
        OpenDU.screen.blit(MCDU, (0,0))

        defaultPage = getattr(__import__(pagesPath, fromlist=[primusEpic.currentPage]), primusEpic.currentPage)
        defaultPage.page()

    def buildMenu(options):

        rect = pygame.Rect(103, 65, 521, 426)
        pygame.draw.rect(OpenDU.screen, (0,0,0), rect)

        side_margin = 110
        top_margin = 80

        text_font_size = 29
        title_font_size = 21
        line_spacing = 8
        options_count = 0
        top_distance = top_margin + title_font_size + 5 + line_spacing + 10
        top_distances = []

        for row in options:

            if options_count == 0:

                # Title
                OpenDU.text(row[0], Suite.font, row[1], (OpenDU.xsize/2), top_margin, text_font_size + 5, "center")

            elif options_count == 1:

                # Page Num
                OpenDU.text(row[0], Suite.font, row[1], (OpenDU.xsize - side_margin), (top_margin + 10), title_font_size, "right")

            else:

                OpenDU.text(row[0][0], Suite.font, row[0][1], side_margin + 23, top_distance, title_font_size)    # Title
                OpenDU.text(row[1][0], Suite.font, row[1][1], side_margin, top_distance + title_font_size + 5, text_font_size)    # Text

                OpenDU.text(row[2][0], Suite.font, row[2][1], (OpenDU.xsize/2), top_distance, title_font_size, "center")
                OpenDU.text(row[3][0], Suite.font, row[3][1], (OpenDU.xsize/2), top_distance + title_font_size + 5, title_font_size, "center")
                
                OpenDU.text(row[4][0], Suite.font, row[4][1], (OpenDU.xsize - side_margin - 23), top_distance, title_font_size, "right")    # Title
                OpenDU.text(row[5][0], Suite.font, row[5][1], (OpenDU.xsize - side_margin), top_distance + title_font_size + 5, text_font_size, "right")    # Text

                top_distance += text_font_size + title_font_size + line_spacing
                top_distances.append(top_distance - line_spacing)

            options_count += 1

        OpenDU.text(OpenDU.scratchpadText, Suite.font, (255,255,255), side_margin, (top_distances[5] + 1), text_font_size, "left")
        
        return top_distances
        
        # Scratchpad
        



