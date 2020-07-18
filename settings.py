import pygame

from src import quad_util

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Size we're trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# Speed for the paddle
PADDLE_SPEED = 200

# Num points base to recover a live
LIVE_POINTS_BASE = 2000

# Number of high scores to show
NUM_HIGHSCORES = 10

POWERUP_SPEED = 50

PADDLE_GROW_UP_POINTS = 200

# Sound effects
GAME_SOUNDS = {
    'paddle_hit': pygame.mixer.Sound('sounds/paddle_hit.wav'),
    'wall_hit': pygame.mixer.Sound('sounds/wall_hit.wav'),
    'brick_hit_1': pygame.mixer.Sound('sounds/brick_hit_1.wav'),
    'brick_hit_2': pygame.mixer.Sound('sounds/brick_hit_2.wav'),
    'hurt': pygame.mixer.Sound('sounds/hurt.wav'),
    'selected': pygame.mixer.Sound('sounds/selected.wav'),
    'life': pygame.mixer.Sound('sounds/life.wav'),
    'high_score': pygame.mixer.Sound('sounds/high_score.wav'),
    'pause': pygame.mixer.Sound('sounds/pause.wav'),
    'level_complete': pygame.mixer.Sound('sounds/level_complete.wav'),
    'unlock_brick': pygame.mixer.Sound('sounds/unlock_brick.wav'),
    'grow_up': pygame.mixer.Sound('sounds/grow_up.wav'),
}

# Graphics
GAME_TEXTURES = {
    'background': pygame.image.load('graphics/background.png'),
    'atlas': pygame.image.load('graphics/breakout.png'),
    'hearts': pygame.image.load('graphics/hearts.png'),
    'arrows': pygame.image.load('graphics/arrows.png'),
}

# Quad frames
GAME_FRAMES = {
    'paddles': quad_util.generate_paddle_quads(),
    'balls': quad_util.generate_ball_quads(),
    'bricks': quad_util.generate_brick_quads(GAME_TEXTURES['atlas']),
    'hearts': quad_util.generate_quads(GAME_TEXTURES['hearts'], 10, 9),
    'arrows': quad_util.generate_quads(GAME_TEXTURES['arrows'], 24, 24),
    'power-ups': quad_util.generate_powerups_quads(),
}

# Fonts
GAME_FONTS = {
    'tiny': pygame.font.Font('fonts/font.ttf', 6),
    'small': pygame.font.Font('fonts/font.ttf', 8),
    'medium': pygame.font.Font('fonts/font.ttf', 12),
    'large': pygame.font.Font('fonts/font.ttf', 24),
}

# Dictionary of pressed keys
pressed_keys = {}

# Variable to indicate that game is paused
paused = False
