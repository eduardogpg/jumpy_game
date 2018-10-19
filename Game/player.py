import pygame
from .settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.vel = 0

        self.jump = False

    def jump(self):
        pass

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos_x -= 10

        if keys[pygame.K_RIGHT]:
            self.pos_x += 10
            
    def update(self):
        self.move()

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
