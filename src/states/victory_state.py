"""
This file contains the implementation of the class VictoryState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/16/2020
"""
import pygame

from garble.state_machine import BaseState
from garble.text import render_text

import settings


class VictoryState(BaseState):
    def enter(self, **params):
        settings.GAME_SOUNDS['level_complete'].play()
        self.lives = params['lives']
        self.level = params['level']
        self.score = params['score']
        self.paddle = params['paddle']
        self.balls = params['balls']
        self.live_factor = params['live_factor']
        self.points_to_next_live = params['points_to_next_live']

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change(
                'serve',
                lives=self.lives,
                level=self.level + 1,
                paddle=self.paddle,
                score=self.score,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor
            )
    
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

        self.paddle.render(surface)

        for ball in self.balls:
            ball.render(surface)

        render_text(
            surface, f'Level {self.level} completed!', settings.GAME_FONTS['large'],
             settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2-30,
             (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press Enter to continue!', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2,
            (255, 255, 255), center=True
        )

