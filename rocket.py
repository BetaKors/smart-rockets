from random import randrange

from engine.colors import *
from engine.core import *
from engine.draw import *
from engine.game import *
from engine.utils import *


class Rocket(Renderable):
    def __init__(self, game: Game, manager, genes=None):
        self.game = game
        self.manager = manager

        self.pos = Vector2(WIDTH // 2, HEIGHT * 0.8)
        self.vel = Vector2()
        self.acc = Vector2()

        self.genes = genes or [
            random_direction() * 2
            for _ in range(self.manager.simulation_duration)
        ]

    @classmethod
    def as_offspring(cls, game: Game, manager, a, b):
        duration = manager.simulation_duration
        mid_point = randint(duration*0.4, duration*0.6)

        genes = [
            *a.genes[:mid_point],
            *b.genes[mid_point:]
        ]

        for _ in range(manager.mutation_quantity):
            index = randrange(0, duration)
            genes[index] = random_direction()
        
        return cls(game, manager, genes)

    @property
    def score(self):
        if hasattr(self, '_reached_when'):
            return 1 / self.pos.distance_to(self.manager.target) * 100 + 1 / self._reached_when * self.manager.simulation_duration
        return 1 / self.pos.distance_to(self.manager.target) * 100
    
    @property
    def has_reached_target(self):
        dist = self.pos.distance_to(self.manager.target)
        return dist < self.manager.target_radius * 2

    def update(self):
        if self.has_reached_target:
            if not hasattr(self, '_reached_when'):
                self._reached_when = self.manager.sim_frame_count
        else:
            self._apply_movement()

        super().update()

    def render(self):
        circle(self.pos, 15, self._get_color())

    def _get_color(self):
        if self.manager.worst == self:
            return red

        if self.manager.best == self:
            return green

        return white

    def _apply_movement(self):
        self._apply_force(self.genes[self.manager.sim_frame_count])
        self.vel += self.acc
        self.pos += limit_vec2_mag(self.vel, 10)
        self.acc = Vector2()

    def _apply_force(self, force):
        self.acc += force
