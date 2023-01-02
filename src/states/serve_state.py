"""
This file contains the implementation of the class ServeState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from gale.state_machine import BaseState
from gale.input_handler import InputHandler, InputListener
from gale.text import render_text

from src.paddle import Paddle
from src.ball import Ball
from src.level_maker import create_level

import settings


class ServeState(BaseState, InputListener):
    def enter(self, **params):
        InputHandler.register_listener(self)
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

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'enter' and input_data.pressed:
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

        elif input_id == 'left':
            if input_data.pressed:
                self.paddle.vx = -settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx < 0:
                self.paddle.vx = 0
        elif input_id == 'right':
            if input_data.pressed:
                self.paddle.vx = settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx > 0:
                self.paddle.vx = 0

    def update(self, dt):
        self.paddle.update(dt)
        self.ball.x = self.paddle.x + self.paddle.width // 2 - 2

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
