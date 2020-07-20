"""
This file contains the implementation of the class Text.

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


class Text:
    def __init__(self, text_str, font, x, y, color,
                 bgcolor=None, center=False):
        self.text_str = text_str
        self.font = font
        self.text = font.render(self.text_str, True, color, bgcolor)
        self.rect = self.text.get_rect()
        self.x = x
        self.y = y
        self.center = center
    
    def render(self, surface):
        if self.center:
            self.rect.center = (self.x, self.y)
        else:
            self.rect.x = self.x
            self.rect.y = self.y
        surface.blit(self.text, self.rect)



