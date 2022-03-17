from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, game) -> None:
        self.game = game

    @abstractmethod
    def update(self) -> None:
        pass

    def should_remove(self) -> bool:
        return False


class Renderable(Component):
    def update(self) -> None:
        self.render()

    @abstractmethod
    def render(self) -> None:
        pass
