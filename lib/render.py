"""
This file contains an utility function to render text.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
def render_text(surface, text, font, x, y, color, bgcolor=None, center=False):
    text_obj = font.render(text, True, color, bgcolor)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y
    surface.blit(text_obj, text_rect)
