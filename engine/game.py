import pygame
from pygame import Vector2

from engine.core import Component

from .colors import *
from .constants import *


class Game:
    def __init__(self):
        self._setup()
        self._frame_count = 0
        self.components: list[Component] = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.dispose()

    @property
    def mouse_pos(self) -> Vector2:
        return Vector2(*pygame.mouse.get_pos())

    @property
    def frame_count(self) -> int:
        return self._frame_count

    def mainloop(self):
        clock = pygame.time.Clock()

        while not self._should_quit():
            self.screen.fill(gray)

            self._cleanup()

            for component in self.components:
                component.update()

            self._frame_count += 1

            pygame.display.update()
            clock.tick(FPS)

    def is_mouse_pressed(self, button: int=None) -> bool:
        buttons = pygame.mouse.get_pressed()
        return any(buttons) if button is None else buttons[button]

    def dispose(self):
        pygame.quit()

    def _setup(self):
        pygame.init()
        pygame.display.set_caption('Game')
        pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen = pygame.display.get_surface()

    def _cleanup(self):
        pred = lambda c: not c.should_remove()
        filtered = filter(pred, self.components)
        self.components = list(filtered)

    def _should_quit(self):
        quit_event = pygame.event.get(pygame.QUIT)
        kdown_event = pygame.event.get(pygame.KEYDOWN)
        has_pressed_esc = kdown_event and kdown_event[0].key == pygame.K_ESCAPE
        return quit_event or has_pressed_esc
