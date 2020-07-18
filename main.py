"""
This file contains the implementation of the game Breakout.

Update:
    - Music
    - Pause
    - Adding lives
    - Pushing the ball

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

from lib.game import Game
from lib.state_machine import StateMachine

import settings

from src import states

class Breakout(Game):
    def init(self):
        self.state_machine = StateMachine({
            'start': states.StartState,
            'paddle_selection': states.PaddleSelectionState,
            'serve': states.ServeState,
            'play': states.PlayState,
            'victory': states.VictoryState,
            'game_over': states.GameOverState,
            'enter_high_score': states.EnterHighScoreState,
            'show_high_score': states.ShowHighScoreState,
        })
        self.state_machine.change('start')
        pygame.mixer_music.load('sounds/music.wav')
        pygame.mixer_music.play(loops=-1)

    def update(self, dt):
        self.state_machine.update(dt)
        settings.pressed_keys = {}

    def render(self, surface):
        surface.blit(
            settings.GAME_TEXTURES['background'], (0, 0)
        )
        self.state_machine.render(surface)

    def keydown(self, key):
        settings.pressed_keys[key] = True

if __name__ == '__main__':
    game = Breakout(
        title='Breakout', window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )
    game.exec()
