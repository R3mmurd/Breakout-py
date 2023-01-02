"""
This file contains the implementation of the class Ball.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import random

import pygame

import settings


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8

        self.vx = 0
        self.vy = 0

        self.texture = settings.GAME_TEXTURES['atlas']
        self.frame = random.randint(0, 6)
        self.in_play = True

    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, obj):
        return self.get_collision_rect().colliderect(
            obj.get_collision_rect()
        )

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Check collision with walls
        if self.x < 0:
            settings.GAME_SOUNDS['wall_hit'].stop()
            settings.GAME_SOUNDS['wall_hit'].play()
            self.x = 0
            self.vx *= -1

        if self.x + self.width > settings.VIRTUAL_WIDTH:
            settings.GAME_SOUNDS['wall_hit'].stop()
            settings.GAME_SOUNDS['wall_hit'].play()
            self.x = settings.VIRTUAL_WIDTH - self.width
            self.vx *= -1

        if self.y < 0:
            settings.GAME_SOUNDS['wall_hit'].stop()
            settings.GAME_SOUNDS['wall_hit'].play()
            self.y = 0
            self.vy *= -1

        if self.y > settings.VIRTUAL_HEIGHT:
            settings.GAME_SOUNDS['hurt'].play()
            self.in_play = False

    def render(self, surface):
        surface.blit(
            self.texture, (self.x, self.y),
            settings.GAME_FRAMES['balls'][self.frame]
        )
