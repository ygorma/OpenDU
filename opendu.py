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
OpenDU.suitePath        = 'suites/' + OpenDU.suite  + '/'
OpenDU.pages            = OpenDU.suitePath + 'pages/'
OpenDU.textures         = OpenDU.suitePath + 'texture/'
OpenDU.frame            = OpenDU.config.getint('main','frame')
OpenDU.conn             = socket.socket()

# Run PyGame
OpenDU.init()

# Main Loop
while True:

    # Key Pressed?
    OpenDU.keyPress()

    # Send Data
    MESSAGE = str("\r\n")
    OpenDU.conn.send(MESSAGE.encode(encoding='utf_8')) 

    # Request Data
    OpenDU.send = {}   # Clean Last
    OpenDU.received = OpenDU.conn.recv(1024)

    # Import Display
    imported = getattr(__import__(OpenDU.suitePackage, fromlist=[OpenDU.suite]), OpenDU.suite)
    imported.Suite.init(OpenDU.config.get('main','page'))

    # Update Screen
    pygame.display.update() 