"""
This file contains the implementation of the class EnterHighScoreState.

Author: Alejandro Mujica (aledrums@gmail.com)
Data: 07/16/2020
"""
import string

import pygame

from gale.state_machine import BaseState
from gale.input_handler import InputHandler, InputListener
from gale.text import render_text

from src.highscores import read_highscores, write_highscores

import settings


class EnterHighScoreState(BaseState, InputListener):
    def enter(self, score):
        InputHandler.register_listener(self)
        self.score = score
        self.hs = read_highscores()

        if (self.score > 0
                and (len(self.hs) < settings.NUM_HIGHSCORES
                     or self.score > self.hs[-1][1])):
            settings.GAME_SOUNDS['high_score'].play()
        else:
            self.state_machine.change('start')

        self.name = [0, 0, 0]
        self.selected = 0

    def exit(self):
        InputHandler.register_unlistener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'enter' and input_data.pressed:
            name = ''.join([string.ascii_uppercase[i] for i in self.name])
            self.hs.append([name, self.score])
            self.hs.sort(key=lambda item: item[-1], reverse=True)
            write_highscores(self.hs[:settings.NUM_HIGHSCORES])
            self.state_machine.change('start')

        if input_id == 'left' and input_data.pressed:
            self.selected = max(0, self.selected - 1)
        elif input_id == 'right' and input_data.pressed:
            self.selected = min(2, self.selected + 1)
        elif input_id == 'down' and input_data.pressed:
            self.name[self.selected] = max(
                0, self.name[self.selected] - 1
            )
        elif input_id == 'up' and input_data.pressed:
            self.name[self.selected] = min(
                len(string.ascii_uppercase)-1,
                self.name[self.selected] + 1
            )

    def render(self, surface):
        render_text(
            surface, f'Final score: {self.score}', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2-100,
            (255, 255, 255), center=True
        )
        render_text(
            surface, f'You are in the top {settings.NUM_HIGHSCORES}!',
            settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2-70,
            (255, 255, 255), center=True
        )
        render_text(
            surface, 'Enter your name', settings.GAME_FONTS['small'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2-20,
            (255, 255, 255), center=True
        )

        x = settings.VIRTUAL_WIDTH//2 - 20

        for i in range(3):
            color = (52, 235, 216) if self.selected == i else (255, 255, 255)

            render_text(
                surface, string.ascii_uppercase[self.name[i]],
                settings.GAME_FONTS['medium'],
                x, settings.VIRTUAL_HEIGHT//2+10,
                color, center=True
            )

            x += 20

        render_text(
            surface, 'Press Enter to finish!', settings.GAME_FONTS['small'],
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT-50,
            (255, 255, 255), center=True
        )
