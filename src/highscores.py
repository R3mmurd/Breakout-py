"""
This file contains utilities to handle the high score file.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/16/2020
"""
import os

import settings

# Path of home user directory
USER_HOME = os.path.expanduser('~')

BREAKOUT_DIR = os.path.join(USER_HOME, '.breakout')

HIGHSCORES_PATH = os.path.join(BREAKOUT_DIR, 'highscores.dat')


def read_highscores():
    if not os.path.exists(BREAKOUT_DIR):
        os.mkdir(BREAKOUT_DIR)

    with open(HIGHSCORES_PATH, 'a'):
        pass

    highscores = []

    with open(HIGHSCORES_PATH, 'r') as f:
        for line in f:
            line = line[:-1]
            line = line.split(':')
            line[-1] = int(line[-1])
            highscores.append(line)

    return highscores


def write_highscores(highscores):
    with open(HIGHSCORES_PATH, 'w') as f:
        for line in highscores:
            line[-1] = str(line[-1])
            line = ':'.join(line)
            f.write(f'{line}\n')
