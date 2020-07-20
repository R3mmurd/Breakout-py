"""
This file contains the implementation of the class StartState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from lib.base_state import BaseState
from lib.text import render_text

import settings

class StartState(BaseState):
    def enter(self):
        self.selected = 1

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            settings.GAME_SOUNDS['selected'].play()
            
            if self.selected == 1:
                self.state_machine.change('paddle_selection')
            else:
                self.state_machine.change('show_high_score')

        if settings.pressed_keys.get(pygame.K_DOWN) and self.selected == 1:
            settings.GAME_SOUNDS['paddle_hit'].play()
            self.selected = 2
        elif settings.pressed_keys.get(pygame.K_UP) and self.selected == 2:
            settings.GAME_SOUNDS['paddle_hit'].play()
            self.selected = 1

    def render(self, surface):
        render_text(
            surface, 'Breakout', settings.GAME_FONTS['large'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//3,
            (255, 255, 255), center=True
        )

        color = (52, 235, 216) if self.selected == 1 else (255, 255, 255)

        render_text(
            surface, 'Play Game', settings.GAME_FONTS['medium'], 
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT-60, 
            color, center=True
        )

        color = (52, 235, 216) if self.selected == 2 else (255, 255, 255)

        render_text(
            surface, 'High scores', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT-30,
            color, center=True
        )
