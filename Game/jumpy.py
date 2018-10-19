from .settings import *
from .player import Player, Platform
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
        self.player = Player( WIDTH / 2, HEIGHT - 80 )
        self.platform = Platform(0, HEIGHT - 40, WIDTH, 40)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.platform)

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

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()
