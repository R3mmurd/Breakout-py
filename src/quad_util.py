"""
This file contains functions to generate quads to get elements
from an "atlas" (a texture with multiple sprites).

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame

def generate_quads(atlas, tile_width, tile_height):
    """
    Given and atlas, this function builds a list of quads based on
    atlas dimensions, tile width, and tile height.

    :param atlas: surace with the texture.
    :param tile_width: with of the sprite.
    :param tile_height: Height of the sprite.
    """
    atlas_width, atlas_height = atlas.get_size()

    num_cols = atlas_width//tile_width
    num_rows = atlas_height//tile_height

    spritesheet = []

    for i in range(num_rows):
        for j in range(num_cols):
            spritesheet.append(
                pygame.Rect(
                    j * tile_width,   # x position
                    i * tile_height,  # y position
                    tile_width, tile_height
                )
            )
    
    return spritesheet


def generate_paddle_quads():
    """
    This function builds a matrix of paddles, each row in the matrix
    represents the paddle skin (four colors) and each column represents
    the size.
    """
    paddle_base_width = 32
    paddle_height = 16

    x = 0
    y = paddle_height * 4

    spritesheet = []

    for _ in range(4):
        spritesheet.append([
            # The smallest paddle is in (0, y) and its dimensions are 32x16.
            pygame.Rect(x, y, paddle_base_width, paddle_height),

            # The next paddle is in (32, y) and its dimensions are 64x16.
            pygame.Rect(
                x + paddle_base_width, y, 
                paddle_base_width * 2, paddle_height
            ),

            # The next paddle is in (96, y) and its dimensions are 96x16.
            pygame.Rect(
                x + paddle_base_width * 3, y, 
                paddle_base_width * 3, paddle_height
            ),

            # The largest paddle is in (0, y + 16)
            # and its dimensions are 128x16.
            pygame.Rect(
                x, y + paddle_height, 
                paddle_base_width * 4, paddle_height
            )
        ])

        # To go to the next color, increment y by 32.
        y += paddle_height * 2

    return spritesheet


def generate_ball_quads():
    """
    This function builds a list of balls.
    """
    ball_size = 8
    x = 96
    y = 48
    
    spritesheet = []

    for _ in range(4):
        spritesheet.append(pygame.Rect(x, y, ball_size, ball_size))
        x += ball_size

    x = 96
    y += ball_size

    for _ in range(3):
        spritesheet.append(pygame.Rect(x, y, ball_size, ball_size))
        x += ball_size

    return spritesheet

def generate_brick_quads(atlas):
    all_quads = generate_quads(atlas, 32, 16)
    # Slice the first 20 quads and add the locked brick
    return all_quads[:20] + [all_quads[23]]

def generate_powerups_quads():
    y = 12 * 16  # 4 brick rows + 8 paddle rows

    spritesheet = []

    for j in range(10):
        spritesheet.append(pygame.Rect(j*16, y, 16, 16))

    return spritesheet
