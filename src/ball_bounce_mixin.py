"""
This file contains the implementation of a mixin that contains a
method that solves the collision between a rectangular shape with
the ball.

Collision solve algorithm taken from:
https://github.com/noooway/love2d_arkanoid_tutorial/wiki/Resolving-Collisions

Author: Alejandro Mujica
Date: 15/07/2020
"""

class BallBounceMixin:
    def get_intersection(self, r1, r2):
        """
        Compute, if exists, the intersection between two
        rectangles.
        """
        if (r1.x > r2.right or r1.right < r2.x
                or r1.bottom < r2.y or r1.y > r2.bottom):
            # There is no intersection
            return None

        # Compute x shift
        if r1.centerx < r2.centerx:
            x_shift = r1.right - r2.x
        else:
            x_shift = r1.x - r2.right

        # Compute y shift
        if r1.centery < r2.centery:
            y_shift = r2.y - r1.bottom
        else:
            y_shift = r2.bottom - r1.y

        return (x_shift, y_shift)

    def rebound(self, ball):
        br = ball.get_collision_rect()
        sr = self.get_collision_rect()
        
        r = self.get_intersection(br, sr)

        if r is None:
            return

        shift_x, shift_y = r

        min_shift = min(abs(shift_x), abs(shift_y))

        if min_shift == abs(shift_x):
            # Collision happened from left or right
            ball.x += shift_x
            ball.vx *= -1
        else:
            # Collision happend from top or bottom
            ball.y += shift_y
            ball.vy *= -1        
