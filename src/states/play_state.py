"""
This file contains the implementation of the class PlayState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import random

import pygame

from lib.state_machine import BaseState
from lib.text import render_text

from src.paddle import Paddle
from src.ball import Ball
from src.level_maker import create_level
from src import powerups

import settings


class PlayState(BaseState):
    def enter(self, **params):
        self.level = params['level']
        self.score = params['score']
        self.lives = params['lives']
        self.paddle = params['paddle']
        self.balls = [params['ball']]
        self.bricks, self.locked_brick = params['bricks']
        self.broken_bricks_counter = params['broken_bricks_counter']

        settings.GAME_SOUNDS['paddle_hit'].play()

        self.balls[0].vx = random.randint(-80, 80)
        self.balls[0].vy = random.randint(-170, -100)

        self.live_factor = params['live_factor']
        self.points_to_next_live = params['points_to_next_live']

        self.points_to_next_grow_up = (
            self.score +
            settings.PADDLE_GROW_UP_POINTS * (self.paddle.size+1) *self.level
        )

        self.powerups = []

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_p):
            settings.GAME_SOUNDS['pause'].play()
            settings.paused = not settings.paused

            if settings.paused:
                pygame.mixer_music.pause()
            else:
                pygame.mixer_music.unpause()
        
        if settings.paused:
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle.vx = -settings.PADDLE_SPEED
        elif keys[pygame.K_RIGHT]:
            self.paddle.vx = settings.PADDLE_SPEED
        else:
            self.paddle.vx = 0

        self.paddle.update(dt)

        ###### BALLS UPDATE  ######

        for ball in self.balls:
            ball.update(dt)

            # if the ball went out of the game, go to the next.
            if not ball.in_play:
                continue

            # Check and solve the collision between the paddle and the ball.
            if ball.collides(self.paddle):
                settings.GAME_SOUNDS['paddle_hit'].stop()
                settings.GAME_SOUNDS['paddle_hit'].play()
                self.paddle.rebound(ball)

                # Push the ball
                br = ball.get_collision_rect()
                pr = self.paddle.get_collision_rect()
                d = pr.centerx - br.x

                if d > 0 and self.paddle.vx < 0 and pr.x > 0:
                    ball.vx = -50 - 8*d
                elif (d < 0 and self.paddle.vx > 0
                        and pr.right < settings.VIRTUAL_HEIGHT):
                    ball.vx = 50 - 8*d

        # Removing die balls
        self.balls = [b for b in self.balls if b.in_play]

        # check for losing a life
        if not self.balls:
            self.lives -= 1

            if self.lives == 0:
                self.state_machine.change('game_over', score=self.score)
            else:
                self.paddle.dec_size()
                self.state_machine.change(
                    'serve',
                    lives=self.lives,
                    level=self.level,
                    score=self.score,
                    paddle=self.paddle,
                    bricks=(self.bricks, self.locked_brick),
                    broken_bricks_counter=self.broken_bricks_counter,
                    points_to_next_live=self.points_to_next_live,
                    live_factor=self.live_factor
                )
    
        ###### Bricks update ######
        
        for brick in self.bricks:
            brick.update(dt)

            # Check the collisions with the balls
            for ball in self.balls:
                if brick.in_play and ball.collides(brick):
                    brick.hit()
                    brick.rebound(ball)

                    self.score += brick.score()

                    # Check earn life
                    if self.score >= self.points_to_next_live:
                        settings.GAME_SOUNDS['life'].stop()
                        settings.GAME_SOUNDS['life'].play()
                        self.lives = min(3, self.lives + 1)
                        self.live_factor += 0.5
                        self.points_to_next_live += (
                            settings.LIVE_POINTS_BASE*self.live_factor
                        )

                    # Check growing up of the paddle
                    if self.score >= self.points_to_next_grow_up:
                        settings.GAME_SOUNDS['grow_up']
                        self.points_to_next_grow_up += (
                            settings.PADDLE_GROW_UP_POINTS 
                            * (self.paddle.size + 1) * self.level
                        )
                        self.paddle.inc_size()

                    # Chance to generate a brick key
                    bricks_in_play = (
                        len(self.bricks) - self.broken_bricks_counter
                    )
                    if (self.locked_brick is not None
                            and random.randint(1, bricks_in_play) == 1):
                        r = brick.get_collision_rect()
                        self.powerups.append(
                            powerups.BrickKey(r.centerx-8, r.centery-8)
                        )
                    # Chance to generate two more balls
                    elif random.random() < 0.05:
                        r = brick.get_collision_rect()
                        self.powerups.append(
                            powerups.TwoMoreBall(r.centerx-8, r.centery-8)
                        )

                    if not brick.in_play:
                        self.broken_bricks_counter += 1        

        # Update powerups
        for powerup in self.powerups:
            powerup.update(dt)

            if powerup.collides(self.paddle):
                powerup.take(self)
        
        self.powerups = [p for p in self.powerups if p.in_play]


        # Check victory
        if self.broken_bricks_counter == len(self.bricks):
            self.state_machine.change(
                'victory',
                lives=self.lives,
                level=self.level,
                score=self.score,
                paddle=self.paddle,
                balls=self.balls,
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

        for brick in self.bricks:
            brick.render(surface)

        self.paddle.render(surface)

        for ball in self.balls:
            ball.render(surface)

        for powerup in self.powerups:
            powerup.render(surface)
