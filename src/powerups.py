"""
This file contains classes to define game power-ups.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/18/2020
"""
import random

import pygame

from src.ball import Ball

import settings


class PowerUp:
    """
    The base power-up.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = settings.POWERUP_SPEED
        self.in_play = True
        self.frame = -1
    
    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, 16, 16)

    def collides(self, obj):
        return self.get_collision_rect().colliderect(
            obj.get_collision_rect()
        )

    def update(self, dt):
        if self.y > settings.VIRTUAL_HEIGHT:
            self.in_play = False

        self.y += self.vy*dt
    
    def render(self, surface):
        surface.blit(
            settings.GAME_TEXTURES['atlas'], (self.x, self.y),
            settings.GAME_FRAMES['power-ups'][self.frame]
        )
    
    def take(self, play_state):
        raise NotImplementedError
    

class BrickKey(PowerUp):
    """
    Power-up to unlock a locked brick.
    """
    def __init__(self, x, y):
        super(BrickKey, self).__init__(x, y)
        self.frame = 9

    def take(self, play_state):
        if play_state.locked_brick is not None:
            settings.GAME_SOUNDS['unlock_brick'].play()
            play_state.locked_brick.locked = False
            play_state.locked_brick = None
        self.in_play = False


class TwoMoreBall(PowerUp):
    """
    Power-up to add two more ball to the game.
    """
    def __init__(self, x, y):
        super(TwoMoreBall, self).__init__(x, y)
        self.frame = 8
    
    def take(self, play_state):
        paddle = play_state.paddle

        for _ in range(2):
            b = Ball(paddle.x + paddle.width//2 - 4, paddle.y - 8)
            settings.GAME_SOUNDS['paddle_hit'].play()

            b.vx = random.randint(-80, 80)
            b.vy = random.randint(-170, -100)
            play_state.balls.append(b)

        self.in_play = False
