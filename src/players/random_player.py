import random

from src.games.game import Game
from src.players.player import Player


class RandomPlayer(Player):

    def __init__(self, name: str = "RandomPlayer"):
        super().__init__(name=name)

    def move(self, game: Game):
        possible_moves = game.board.get_possible_moves()
        return random.choice(possible_moves)
