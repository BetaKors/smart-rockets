import pygame
from pygame import gfxdraw, freetype

from .colors import *


def text(pos, txt, color=white, font_name='Arial', font_size=20):
    font = freetype.SysFont(font_name, font_size)

    font.render_to(
        _get_surface(),
        pos,
        str(txt),
        color
    )


def square(pos, size, color=white):
    rect = pygame.Rect(0, 0, size, size)

    rect.center = pos

    pygame.draw.rect(
        _get_surface(),
        color,
        rect
    )


def rect(pos, width, height, color=white):
    rect = pygame.Rect(0, 0, width, height)

    rect.center = pos

    pygame.draw.rect(
        _get_surface(),
        color,
        rect
    )


def circle(pos, radius, color=white, antialiasing=True):
    if antialiasing:
        int_pos = tuple(map(int, pos))

        gfxdraw.aaellipse(
            _get_surface(),
            *int_pos,
            radius+1,
            radius,
            color
        )

        gfxdraw.filled_circle(
            _get_surface(),
            *int_pos,
            radius,
            color
        )
    else:
        pygame.draw.circle(
            _get_surface(),
            color,
            pos,
            radius
        )


def _get_surface():
    return pygame.display.get_surface()
