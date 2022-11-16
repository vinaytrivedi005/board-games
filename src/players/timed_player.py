from abc import abstractmethod

from src.players.player import Player


class TimedPlayer(Player):

    def __init__(self, name: str = "TimedPlayer"):
        super().__init__(name=name)

    @abstractmethod
    def move(self, game, time_for_move=1):
        pass
