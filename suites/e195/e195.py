
from app.lib.defs import *

class Suite:

    font = OpenDU.suitePath + "fonts\\primusEpic.ttf"

    def init(page):

        pagesPath = 'suites.e195.pages'

        defaultPage = getattr(__import__(pagesPath, fromlist=[page]), page)
        defaultPage.primusEpic.init()