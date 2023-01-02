"""
This file contains the implementation of the class GameOverState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from gale.state_machine import BaseState
from gale.input_handler import InputHandler, InputListener
from gale.text import render_text

import settings


class GameOverState(BaseState, InputListener):
    def enter(self, score):
        InputHandler.register_listener(self)
        self.score = score

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'enter' and input_data.pressed:
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
