"""
This file contains the implementation of the class ShowHighScoreState.

Author: Alejandro Mujica (aledrums@gmail.com)
Data: 07/16/2020
"""
import pygame

from lib.base_state import BaseState
from lib.text import render_text

from src.highscores import read_highscores

import settings


class ShowHighScoreState(BaseState):
    def enter(self):
        self.hs = read_highscores()
        
    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change('start')

    def render(self, surface):
        render_text(
            surface, 'High Scores', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, 20,
            (255, 255, 255), center=True
        )
        
        for i in range(settings.NUM_HIGHSCORES):
            name = '---'
            score = '---'
        
            if i < len(self.hs):
                item = self.hs[i]
                name = item[0]
                score = str(item[1])

            render_text(
                surface, f'{i + 1}.', settings.GAME_FONTS['small'],
                settings.VIRTUAL_WIDTH//2 - 60, 50 + i*17,
                (255, 255, 255), center=True
            )
            render_text(
                surface, name, settings.GAME_FONTS['small'],
                settings.VIRTUAL_WIDTH//2, 50 + i*17,
                (255, 255, 255), center=True
            )
            render_text(
                surface, score, settings.GAME_FONTS['small'],
                settings.VIRTUAL_WIDTH//2 + 60, 50 + i*17,
                (255, 255, 255), center=True
            )
