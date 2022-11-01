import random

from src.games.game import Game
from src.players.player import Player


class HumanPlayer(Player):

    def __init__(self, name: str = "HumanPlayer"):
        super().__init__(name=name)

    def move(self, game: Game):
        possible_moves = game.board.get_possible_moves()
        move = ""
        while move not in possible_moves:
            move = input(f"please enter your move out of possible moves {possible_moves} :")
        return move
