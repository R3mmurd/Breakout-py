"""
This file contains the implementation of the class ServeState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from lib.base_state import BaseState
from lib.render import render_text

from src.paddle import Paddle
from src.ball import Ball
from src.level_maker import create_level

import settings

class ServeState(BaseState):
    def enter(self, **params):
        self.level = params['level']
        self.paddle = params['paddle']
        self.paddle.x = settings.VIRTUAL_WIDTH//2-32
        self.paddle.y = settings.VIRTUAL_HEIGHT-32
        self.ball = Ball(
            self.paddle.x + self.paddle.width//2 - 4, self.paddle.y - 8
        )
        self.bricks = params.get('bricks', create_level(self.level))
        self.score = params.get('score', 0)
        self.lives = params.get('lives', 3)
        self.broken_bricks_counter = params.get('broken_bricks_counter', 0)
        self.live_factor = params.get('live_factor', 1)
        self.points_to_next_live = params.get(
            'points_to_next_live', settings.LIVE_POINTS_BASE
        )

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change(
                'play',
                level=self.level,
                paddle=self.paddle,
                ball=self.ball,
                score=self.score,
                lives=self.lives,
                bricks=self.bricks,
                broken_bricks_counter=self.broken_bricks_counter,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor
            )

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.paddle.vx = -settings.PADDLE_SPEED
        elif keys[pygame.K_RIGHT]:
            self.paddle.vx = settings.PADDLE_SPEED
        else:
            self.paddle.vx = 0

        self.paddle.update(dt)
        self.ball.x = self.paddle.x + self.paddle.width//2 - 2

    def render(self, surface):
        
        heart_x = settings.VIRTUAL_WIDTH-120

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(
                settings.GAME_TEXTURES['hearts'], (heart_x, 5),
                settings.GAME_FRAMES['hearts'][0]
            )
            heart_x += 11
            i += 1
        
        # Draw empty hearts
        while i < 3:
            surface.blit(
                settings.GAME_TEXTURES['hearts'], (heart_x, 5),
                settings.GAME_FRAMES['hearts'][1]
            )
            heart_x += 11
            i += 1

        render_text(
            surface, f'Score: {self.score}', settings.GAME_FONTS['tiny'],
            settings.VIRTUAL_WIDTH-80, 5, (255, 255, 255)
        )

        for brick in self.bricks[0]:
            brick.render(surface)

        self.paddle.render(surface)
        self.ball.render(surface)

        render_text(
            surface, f'Level {self.level}', settings.GAME_FONTS['large'],
             settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2-30,
             (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press Enter to serve!', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2,
            (255, 255, 255), center=True
        )
