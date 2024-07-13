from msilib.schema import Class
from suites.instructor.instructor import *

class Instructor:

    def init():

        pageBegin = Suite.renderMenu()

        image = pygame.image.load(OpenDU.textures + 'plane.svg')
        DEFAULT_IMAGE_POSITION = (200,200)
        image = pygame.transform.rotate(image, 30)
        OpenDU.screen.blit(image, DEFAULT_IMAGE_POSITION)

        Suite.renderBottomMenu()
        Suite.dialogs()