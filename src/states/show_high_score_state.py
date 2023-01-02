"""
This file contains the implementation of the class ShowHighScoreState.

Author: Alejandro Mujica (aledrums@gmail.com)
Data: 07/16/2020
"""
import pygame

from gale.state_machine import BaseState
from gale.input_handler import InputHandler, InputListener
from gale.text import render_text

from src.highscores import read_highscores

import settings


class ShowHighScoreState(BaseState, InputListener):
    def enter(self):
        InputHandler.register_listener(self)
        self.hs = read_highscores()

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'enter' and input_data.pressed:
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
