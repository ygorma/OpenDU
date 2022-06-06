#!/usr/bin/python3.7
import os, sys
import time
import configparser
import socket
import pickle

# Bibliotecas
from app.lib.defs import *
from app.lib.splash import *

# Ler Arquivo INI
OpenDU.config = configparser.ConfigParser()
OpenDU.config.read('opendu.ini')

# Caminhos e Variaveis
OpenDU.path             = os.path.dirname(os.path.realpath(__file__))
OpenDU.suitePackage     = 'suites.' + OpenDU.config.get('main','suite') + ''
OpenDU.suite            = OpenDU.config.get('main','suite')
OpenDU.suitePath        = 'suites/' + OpenDU.suite  + '/'
OpenDU.pages            = OpenDU.suitePath + 'pages/'
OpenDU.textures         = OpenDU.suitePath + 'texture/'
OpenDU.frame            = OpenDU.config.getint('main','frame')

# Splash
if OpenDU.config.getint('main','splash'):
    Splash.init()

# Inicializar PyGame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Posicao da Tela
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (OpenDU.config.getint('main','xposition'),OpenDU.config.getint('main','yposition'))
os.environ['SDL_VIDEO_CENTERED'] = '0'

# Configuracao da Tela
pygame.display.set_caption('OpenDU - ' + OpenDU.config.get('main','window_name'))

if OpenDU.frame == 1:
    OpenDU.screen = pygame.display.set_mode((OpenDU.config.getint('main','xsize'),OpenDU.config.getint('main','ysize')),pygame.RESIZABLE)
else:
    OpenDU.screen = pygame.display.set_mode((OpenDU.config.getint('main','xsize'),OpenDU.config.getint('main','ysize')),pygame.NOFRAME)

OpenDU.text('Trying to Connect on '+ OpenDU.config.get('conn','server') +':'+ OpenDU.config.get('conn','port') +'...', OpenDU.config.get('main','font'), (255,255,255), 10, 10)
pygame.display.update()

# Criar Conexao
Conn = socket.socket()
Conn.connect((OpenDU.config.get('conn','server'), OpenDU.config.getint('conn','port'))) 

OpenDU.text('Connection Acquired!', OpenDU.config.get('main','font'), (255,255,255), 10, 10)
pygame.display.update()
time.sleep(2)

# Loop Principal
running = True

while running:

    # Receber Dados
    OpenDU.send = {}   # Limpar Arranjo
    OpenDU.received = pickle.loads(Conn.recv(1024))

    # Configuracao da Tela
    OpenDU.xsize, OpenDU.ysize = OpenDU.screen.get_size()

    #if OpenDU.frame == 1:
        #OpenDU.screen = pygame.display.set_mode((xsize,ysize),pygame.RESIZABLE)
    #else:
        #OpenDU.screen = pygame.display.set_mode((xsize,ysize),pygame.NOFRAME)

    imported = getattr(__import__(OpenDU.suitePackage, fromlist=[OpenDU.suite]), OpenDU.suite)
    imported.Suite.init(OpenDU.config.get('main','page'))

    # Atualizar Tela
    pygame.display.update()

    # Ao pressionar
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #ESQ
                running = False
            if event.key == pygame.K_TAB: #TAB
                if OpenDU.frame:
                    OpenDU.frame = 0
                else:
                    OpenDU.frame = 1
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            OpenDU.screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
    
    pygame.event.pump()

    # Enviar Solicitacao
    Conn.sendall(pickle.dumps(OpenDU.send))

# Encerrar Conexao
Conn.close()

# Salvar Configuracoes
position = os.environ['SDL_VIDEO_WINDOW_POS']
xcoordinate, ycoordinate = position.split(',')
print(pygame.display.Info())
OpenDU.config.set('main', 'xposition', str(xcoordinate))
OpenDU.config.set('main', 'yposition', str(ycoordinate))
OpenDU.config.set('main', 'xsize', str(OpenDU.xsize))
OpenDU.config.set('main', 'ysize', str(OpenDU.ysize))
OpenDU.config.set('main', 'frame', str(OpenDU.frame))

with open('opendu.ini', 'w') as configfile:
    OpenDU.config.write(configfile)

# Fechar OpenDU
pygame.quit()
      