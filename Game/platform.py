import pygame
from .settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
