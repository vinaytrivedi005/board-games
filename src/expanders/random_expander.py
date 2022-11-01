import random

from src.evaluators.evaluator import Evaluator
from src.expanders.expander import Expander


class RandomExpander(Expander):

    def __init__(self, evaluator: Evaluator):
        super().__init__(evaluator)
        self.is_pondering = False

    def search(self, game, time_for_move=60):
        while True:
            board = game.board
            possible_moves = board.get_possible_moves()
            return random.choice(possible_moves)
