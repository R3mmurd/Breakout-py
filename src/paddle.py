"""
This file contains the implementation of the class Paddle,

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

import settings

from src.ball_bounce_mixin import BallBounceMixin

class Paddle(BallBounceMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 16

        # By default, the blue paddle
        self.skin = 0

        # By default, the 64-pixels-width paddle.
        self.size = 1

        self.texture = settings.GAME_TEXTURES['atlas']
        self.frames = settings.GAME_FRAMES['paddles']
        
        # The paddle only move horizontally
        self.vx = 0

    def resize(self, size):
        self.size = size
        self.width = (self.size + 1) * 32

    def dec_size(self):
        self.resize(max(0, self.size-1))

    def inc_size(self):
        self.resize(min(3, self.size+1))
    
    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt):
        next_x = self.x + self.vx*dt
        
        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)

    def render(self, surface):
        surface.blit(
            self.texture, (self.x, self.y),
            self.frames[self.skin][self.size]
        )