from .settings import *
from .player import Player
from .platform import Platform

import random
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
        self.font_name = pygame.font.match_font(FONT_NAME)

    def new(self):
        self.score = 0
        self.player = Player(self, WIDTH / 2, HEIGHT / 2 )

        self.sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.sprites.add(self.player)

        for platform_config in PLATFORM_LIST:
            platform = Platform(*platform_config)
            self.sprites.add(platform)
            self.platforms.add(platform)

        self.playing = True

        self.run()

    def run(self):
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

        #if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)

                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score +=10

        #spawn new platforms to keep same overage bumber
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-50, -30), width, 20)

            self.platforms.add(p)
            self.sprites.add(p)

        #Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.sprites:
                sprite.rect.y -= max(self.player.vel.y , 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()

        if len(self.platforms) == 0:
            self.playing = False
            self.new()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BLACK)
        self.sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        pygame.display.flip()
