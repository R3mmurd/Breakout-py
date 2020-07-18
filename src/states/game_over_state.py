"""
This file contains the implementation of the class GameOverState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from lib.base_state import BaseState
from lib.render import render_text

import settings


class GameOverState(BaseState):
    def enter(self, score):
        self.score = score

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change('enter_high_score', score=self.score)
    
    def render(self, surface):
        render_text(
            surface, 'Game Over', settings.GAME_FONTS['large'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2-30,
            (255, 255, 255), center=True
        )
        render_text(
            surface, f'Final Score: {self.score}', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2,
            (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press Enter!', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 + 20,
            (255, 255, 255), center=True
        )