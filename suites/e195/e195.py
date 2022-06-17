class Suite:

    def init(page):

        pagesPath = 'suites.e195.pages'

        defaultPage = getattr(__import__(pagesPath, fromlist=[page]), page)
        defaultPage.eJets.init()