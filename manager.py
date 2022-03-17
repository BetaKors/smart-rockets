from engine.core import *
from engine.draw import *
from engine.game import *
from engine.utils import *

from random import randint
from rocket import Rocket


class RocketManager(Renderable):
    target = Vector2(WIDTH // 3, HEIGHT // 10)
    target_radius = 20

    simulation_duration = 200
    mutation_quantity = 2
    population = 100

    def __init__(self, game: Game):
        self.game = game
        self.nsimulations = 0

    @property
    def best(self):
        return max(
            self._filter_rockets(),
            key=lambda r: r.score
        )

    @property
    def worst(self):
        return min(
            self._filter_rockets(),
            key=lambda r: r.score
        )

    @property
    def nrockets_reached_target(self):
        n = 0

        for rocket in self._filter_rockets():
            if rocket.has_reached_target:
                n += 1

        return n

    @property
    def sim_frame_count(self):
        return self.game.frame_count % self.simulation_duration

    def update(self):
        if self._should_update_sim():
            mid_point = randint(
                self.population*0.3,
                self.population*0.5
            )

            best_rockets = self._sort_best_rockets()[:mid_point]

            self.game.components[:] = self._generate_new_population(best_rockets)

            self.game.components.insert(0, self)

            self.nsimulations += 1

        super().update()
    
    def render(self):
        circle(self.target, self.target_radius * 2, light_blue)

        txts = [
            f'Best: {self.best.score:.3f}',
            f'Worst: {self.worst.score:.3f}',
            f'Reached: {self.nrockets_reached_target}',
            f'NSimulations: {self.nsimulations}'
        ]

        for i in range(len(txts)):
            text(
                (40, (i + 1) * 40),
                txts[i]
            )
        
        text(
            (WIDTH-60, HEIGHT-40),
            self.sim_frame_count
        )

    def _should_update_sim(self):
        has_started = self.game.frame_count > 0
        is_sim_done = self.sim_frame_count == 0
        return has_started and is_sim_done

    def _sort_best_rockets(self):
        return sorted(
            self._filter_rockets(),
            key=lambda r: r.score,
            reverse=True
        )

    def _generate_new_population(self, best_rockets):
        return [
            self._generate_offspring(*random_choices(best_rockets, 2))
            for _ in range(self.population)
        ]

    def _generate_offspring(self, a, b):
        return Rocket.as_offspring(self.game, self, a, b)

    def _filter_rockets(self):
        return filter(
            lambda c: isinstance(c, Rocket),
            self.game.components
        )
