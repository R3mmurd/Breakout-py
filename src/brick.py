"""
This file contains the implementation of the class Brick.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/15/2020
"""
import pygame

from gale.particle_system import ParticleSystem

import settings

from src.ball_bounce_mixin import BallBounceMixin

COLOR_PALETTE = (
    (99, 155, 255),   # blue
    (106, 190, 47),   # green
    (217, 87, 99),    # red
    (215, 123, 186),  # purple
    (251, 242, 54)    # gold
)


class Brick(BallBounceMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 16

        self.texture = settings.GAME_TEXTURES['atlas']

        self.tier = 0   # [0, 3]
        self.color = 0  # [0, 4]

        # To decide whether render it or not and collision detection
        self.in_play = True

        self.locked = False

        self.particle_system = ParticleSystem(self.x + 16, self.y + 8, 64)
        self.particle_system.set_life_time(0.2, 0.4)
        self.particle_system.set_linear_acceleration(-0.3, 0.5, 0.3, 1)
        self.particle_system.set_area_spread(4, 7)

    def hit(self):
        settings.GAME_SOUNDS['brick_hit_2'].stop()
        settings.GAME_SOUNDS['brick_hit_2'].play()

        if self.locked:
            return

        r, g, b = COLOR_PALETTE[self.color]
        self.particle_system.set_colors([(r, g, b, 10), (r, g, b, 50)])
        self.particle_system.generate()

        if self.tier == 0:
            if self.color == 0:
                self.in_play = False
                settings.GAME_SOUNDS['brick_hit_1'].stop()
                settings.GAME_SOUNDS['brick_hit_1'].play()
            else:
                self.tier = 3
                self.color -= 1
        else:
            self.tier -= 1

    def score(self):
        if self.locked:
            return 0
        return self.tier*200 + (self.color+1)*25

    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt):
        self.particle_system.update(dt)

    def render(self, surface):
        if self.in_play:
            frame = 20 if self.locked else self.color * 4 + self.tier
            surface.blit(
                self.texture, (self.x, self.y),
                settings.GAME_FRAMES['bricks'][frame]
            )
        self.particle_system.render(surface)
