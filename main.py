from engine.game import Game
from manager import RocketManager
from rocket import Rocket


with Game() as game:
    manager = RocketManager(game)

    game.components.append(manager)

    for _ in range(manager.population):
        game.components.append(Rocket(game, manager))

    game.mainloop()

# TODO rocket manager component to manage smart rockets and update them
