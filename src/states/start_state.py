"""
This file contains the implementation of the class StartState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from gale.state_machine import BaseState
from gale.input_handler import InputHandler, InputListener
from gale.text import render_text

import settings


class StartState(BaseState, InputListener):
    def enter(self):
        InputHandler.register_listener(self)
        self.selected = 1

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'enter' and input_data.pressed:
            settings.GAME_SOUNDS['selected'].play()

            if self.selected == 1:
                self.state_machine.change('paddle_selection')
            else:
                self.state_machine.change('show_high_score')

        if input_id == 'down' and input_data.pressed and self.selected == 1:
            settings.GAME_SOUNDS['paddle_hit'].play()
            self.selected = 2
        elif input_id == 'up' and input_data.pressed and self.selected == 2:
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
