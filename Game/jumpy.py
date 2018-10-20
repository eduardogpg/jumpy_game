from .settings import *
from .player import Player
from .platform import Platform

import pygame

class Jumpy:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT ))
        self.clock =  pygame.time.Clock()
        self.running = True
        self.playing = False

        pygame.display.set_caption(TITLE)

    def new(self):
        self.player = Player(self, WIDTH / 2, HEIGHT / 2 )
        self.platform = Platform(0, HEIGHT - 40, WIDTH, 40)
        p2 = Platform(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)

        self.sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.sprites.add(self.player)
        self.sprites.add(self.platform)
        self.sprites.add(p2)

        self.platforms.add(self.platform)
        self.platforms.add(p2)

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self):
        self.sprites.update()
        #check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

    def draw(self):
        self.screen.fill(BLACK)
        self.sprites.draw(self.screen)

        pygame.display.flip()
