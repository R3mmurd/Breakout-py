"""
This file contains the implementation of a basic class
to implement a Game.

Author: Alejandro Mujica
Date: 07/13/2020
"""
import sys

import pygame

from .timer import Timer

pygame.init()


class Game:
    def __init__(
        self, title=None, window_width=800, window_height=600,
        virtual_width=None, virtual_height=None, *args, **kwargs
    ):
        self.window_width = window_width
        self.window_height = window_height
        self.virtual_width = virtual_width or self.window_width
        self.virtual_height = virtual_height or self.window_height
            
        # Setting the screen
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height), *args, **kwargs
        )
        self.title = title or 'Game'
        pygame.display.set_caption(self.title)
        
        # Creating the virtual screen
        self.surface = pygame.Surface(
            (self.virtual_width, self.virtual_height)
        )
        self.clock = pygame.time.Clock()

        self.running = False

        self.init()

    def init(self):
        pass

    def update(self, dt):
        pass

    def render(self, surface):
        pass

    def keydown(self, key):
        pass

    def _render(self):
        self.surface.fill((0, 0, 0))
        self.render(self.surface)
        self.screen.blit(
            pygame.transform.scale(self.surface, self.screen.get_size()),
            (0, 0)
        )
        pygame.display.update()

    def exec(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
                elif event.type == pygame.KEYDOWN:
                    self.keydown(event.key)
            
            dt = self.clock.tick() / 1000
            Timer.update(dt)
            self.update(dt)
            self._render()

        pygame.quit()

    def quit(self):
        self.running = False
