#!/usr/bin/python3.7
from app.lib.defs import *

# Read INI file
OpenDU.config = configparser.ConfigParser()
OpenDU.config.read('opendu.ini')

# Paths and Vars
OpenDU.path             = os.path.dirname(os.path.realpath(__file__))
OpenDU.logPath          = OpenDU.path +'/opendu.log'
OpenDU.suitePackage     = 'suites.' + OpenDU.config.get('main','suite') + ''
OpenDU.suite            = OpenDU.config.get('main','suite')
OpenDU.suitePath        = OpenDU.path + '\\suites\\' + OpenDU.suite  + '\\'
OpenDU.pages            = OpenDU.suitePath + 'pages\\'
OpenDU.actualPage       = OpenDU.config.get('main','page')
OpenDU.textures         = OpenDU.suitePath + 'texture\\'
OpenDU.frame            = OpenDU.config.getint('main','frame')
OpenDU.fullscreen       = OpenDU.config.getint('main','fullscreen')
OpenDU.brightness       = OpenDU.config.getint('main','brightness')
OpenDU.conn             = socket.socket()
OpenDU.scratchpadText   = ""

# Run PyGame
OpenDU.init()

# Main Loop
while True:

    # Clear Last Image
    OpenDU.clearScreen()

    # Key Pressed?
    OpenDU.keyPress()

    # Connection with Simulator
    if OpenDU.config.getint('main','standalone') == 0:

        # Send Data
        MESSAGE = str("\r\n")
        OpenDU.conn.send(MESSAGE.encode(encoding='utf_8')) 

        # Request Data
        OpenDU.send = {}   # Clean Last
        OpenDU.received = OpenDU.conn.recv(1024)

    # Import Display
    imported = getattr(__import__(OpenDU.suitePackage, fromlist=[OpenDU.suite]), OpenDU.suite)
    imported.Suite.init(OpenDU.actualPage)

    # Brightness Adjustment
    if OpenDU.brightness != 0:
        rect = pygame.Surface((OpenDU.screen.get_width(),OpenDU.screen.get_height()), pygame.SRCALPHA, 32)
        rect.fill((0, 0, 0, OpenDU.brightness))
        OpenDU.screen.blit(rect, (0,0))

    # Print FPS
    OpenDU.fpsCounter()

    # Update Screen
    pygame.display.update() 