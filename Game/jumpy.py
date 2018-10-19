from .settings import *
import pygame

class Jumpy:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT ))
        self.clock =  pygame.time.Clock()
        self.running = True

        pygame.display.set_caption(TITLE)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
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
        pass

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()
