"""
This file contains the implementation of the class Animation.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/19/2020
"""
class Animation:
    def __init__(self, frames, time_interval=0, loops=None):
        self.frames = frames
        self.interval = time_interval
        self.loops = loops
        self.size = len(self.frames)
        self.timer = 0
        self.times_played = 0
        self.current_frame = 0

    def reset(self):
        self.times_played = 0
        self.timer = 0
        self.current_frame = 0

    def update(self, dt):
        if ((self.loops is not None and self.times_played > self.loops)
                or self.size == 1):
            return
        
        self.timer += dt

        if self.timer >= self.interval:
            self.timer %= self.interval
            self.current_frame = (self.current_frame + 1) % self.size

            if self.current_frame == 0:
                self.times_played += 1

    def get_current_frame(self):
        return self.frames[self.current_frame]