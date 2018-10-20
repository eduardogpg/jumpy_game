import pygame
from .settings import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos_x=0, pos_y=0):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        #How many pixel move
        self.pos = vec(pos_x, pos_y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        #jump only stanting on a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1

        if hits:
            self.vel.y = -20

    def move(self):
        self.acc = vec(0, 0.5)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC

        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        self.move()
