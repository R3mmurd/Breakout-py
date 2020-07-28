"""
This class contains the implementation of the class PaddleSelectionState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/16/2020
"""
import pygame

from gale.state_machine import BaseState
from gale.text import render_text

import settings
from src.paddle import Paddle


class PaddleSelectionState(BaseState):
    def enter(self):
        self.paddle = Paddle(
            settings.VIRTUAL_WIDTH//2-32,
            settings.VIRTUAL_HEIGHT-64
        )
        self.arrows_texture = settings.GAME_TEXTURES['arrows']
        self.gray_scale_surface = pygame.Surface((24, 24), pygame.SRCALPHA)

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change(
                'serve', level=1, paddle=self.paddle
            )

        if settings.pressed_keys.get(pygame.K_RIGHT):
            self.paddle.skin = min(3, self.paddle.skin + 1)
        elif settings.pressed_keys.get(pygame.K_LEFT):
            self.paddle.skin = max(0, self.paddle.skin - 1)

    def render(self, surface):

        render_text(
            surface, 'Select a paddle color with left and right', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, 20,
            (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press Enter to continue!', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH//2, 50,
            (255, 255, 255), center=True
        )

        self.paddle.render(surface)

        surface.blit(
            self.arrows_texture,
            (settings.VIRTUAL_WIDTH//2-72-24, settings.VIRTUAL_HEIGHT-68),
            settings.GAME_FRAMES['arrows'][0]
        )

        if self.paddle.skin == 0:
            pygame.draw.circle(
                self.gray_scale_surface, (40, 40, 40, 150), (12, 12), 12
            )
            surface.blit(
                self.gray_scale_surface,
                (settings.VIRTUAL_WIDTH//2-72-24, settings.VIRTUAL_HEIGHT-68)
            )

        surface.blit(
            self.arrows_texture,
            (settings.VIRTUAL_WIDTH//2+72, settings.VIRTUAL_HEIGHT-68),
            settings.GAME_FRAMES['arrows'][1]
        )

        if self.paddle.skin == 3:
            pygame.draw.circle(
                self.gray_scale_surface, (40, 40, 40, 150), (12, 12), 12
            )
            surface.blit(
                self.gray_scale_surface,
                (settings.VIRTUAL_WIDTH//2+72, settings.VIRTUAL_HEIGHT-68)
            )
