from random import randint, uniform, choice

from pygame import Vector2

from .constants import *


def is_point_visible(pos: Vector2) -> bool:
    # horizontal visibility
    hv = pos.x > 0 and pos.x < WIDTH
    # vertical visibility
    vv = pos.y > 0 and pos.y < HEIGHT
    return hv and vv


def is_circle_visible(pos: Vector2, radius: int) -> bool:
    # horizontal visibility
    hv = pos.x > -radius and pos.x < WIDTH + radius
    # vertical visibility
    vv = pos.y > -radius and pos.y < HEIGHT + radius
    return hv and vv


def limit_vec2_mag(vec: Vector2, limit: float) -> Vector2:
    if vec.magnitude() > limit:
        return set_vec2_mag(vec, limit)
    return vec


def set_vec2_mag(vec: Vector2, mag: float) -> Vector2:
    return vec.normalize() * mag


def random_choices(sequence, quantity):
    choices = []

    for _ in range(quantity):
        choices.append(choice(sequence))

    return choices


def random_position(dist_from_border=0) -> Vector2:
    return Vector2(
        randint(dist_from_border, WIDTH - dist_from_border),
        randint(dist_from_border, HEIGHT - dist_from_border)
    )


def random_direction() -> Vector2:
    return Vector2(
        uniform(-1, 1),
        uniform(-1, 1)
    ).normalize()


def random_color() -> tuple[int, int, int]:
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )
